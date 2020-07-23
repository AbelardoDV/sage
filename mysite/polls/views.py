from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import SageSitesTable

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from .models import Sage_lncel
from .models import Sage_wcel
from .models import Sage_bts
from .models import Adyacencias3G
from .models import SageSites
from .models import SageSitesFilter
from .models import SageVoronoiPolygons
from django.core.serializers import serialize
import psycopg2

# Create your views here.

host = "localhost"
database = "Practicando"
user = "postgres"
pwd = "nemuuser"


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class Get_tiers_view(SingleTableMixin, FilterView):
    model = SageSites
    table_class = SageSitesTable
    template_name = 'pages/get_tiers.html'
    filterset_class = SageSitesFilter
    paginate_by = 9


def geojson_sage_lncel(request):
    sage_lncel = serialize('geojson', Sage_lncel.objects.all().filter(sitename='MICAELA_BASTIDAS_TUPAC_AMARU'), fields=["sector"])
    return HttpResponse(sage_lncel, content_type='json')


def geojson_first_tier(request,site_same):
	single_site_voronoi=SageVoronoiPolygons.objects.filter(site_name=site_same).values_list("poligonos")
	json_first_tier = serialize('geojson',SageVoronoiPolygons.objects.filter(poligonos__intersects=single_site_voronoi),fields=["poligonos"])
	return HttpResponse(json_first_tier,content_type="json")


def dibujar_3g_adj(request):
    Adyacencias3G.objects.all().delete()
    conn = psycopg2.connect(host=host,
                            database=database,
                            user=user,
                            password=pwd,
                            port="5432")
    c = conn.cursor()
    query = [''' COPY adyacencias_3g(source_id,target_id) 
FROM 'D:\Proyecto_Visualizacion_PostgreSQL\Web_Adyacencias3G_PostGreSQL.csv' DELIMITER ',' CSV HEADER;''',
             ''' with diagramas as (SELECT webcell_3g.rncid as source_rncid,
				webcell_3g.lat_site as source_lat,
				webcell_3g.lon_site as source_lon,
				webcell_3g.prach_km as source_prach,
				webcell_3g.az as source_az,
				webcell_3g.rd as source_rd,
				adyacencias_3g.source_id as source_id, 
				adyacencias_3g.target_id as target_id,
				webcell_3g_1.rncid as target_rncid,
				webcell_3g_1.lat_site as target_lat,
				webcell_3g_1.lon_site as target_lon,
				webcell_3g_1.prach_km as target_prach,
				webcell_3g_1.az as target_az,
				webcell_3g_1.rd as target_rd
FROM WebCell_3G AS webcell_3g_1 INNER JOIN (webcell_3g INNER JOIN adyacencias_3g 
											ON webcell_3g.LcrId = adyacencias_3g.source_id) 
	ON webcell_3g_1.LcrId = adyacencias_3g.target_id
GROUP BY  		webcell_3g.rncid,
				webcell_3g.lat_site,
				webcell_3g.lon_site,
				webcell_3g.prach_km,
				webcell_3g.az,
				webcell_3g.rd,
				adyacencias_3g.source_id,
				adyacencias_3g.target_id,
				webcell_3g_1.rncid,
				webcell_3g_1.lat_site,
				webcell_3g_1.lon_site,
				webcell_3g_1.prach_km,
				webcell_3g_1.az,
				webcell_3g_1.rd
				) 
	
        UPDATE adyacencias_3g 
        SET linea=ST_MAKELINE(array[st_project( ST_SETSRID(ST_POINT(source_lon, source_lat), 4326),source_rd*1000,radians(source_az))::geometry ,
                                st_project( ST_SETSRID(ST_POINT(target_lon, target_lat), 4326),target_rd*1000,radians(target_az))::geometry])
        ,source_rncid=diagramas.source_rncid
        ,target_rncid=diagramas.target_rncid
        from diagramas
        WHERE adyacencias_3g.source_id=diagramas.source_id AND adyacencias_3g.target_id=diagramas.target_id
        ;''']
    for m in range(len(query)):
        print(query[m])
        c.execute(query[m], vars=None)
        conn.commit()

    conn.close()

    return HttpResponse('ok', content_type='text/plain')


def draw_lncel(request):
    Sage_lncel.objects.all().delete()
    conn = psycopg2.connect(host=host,
                            database=database,
                            user=user,
                            password=pwd,
                            port="5432")

    c = conn.cursor()
    query = ['DELETE FROM sage_lncel', ''' COPY sage_lncel(DL_CH,SiteName,CellName,LAT_SITE,LON_SITE,AZ,BW,RD,RD_normal,separar,MME,MME_ID,lnBtsId,Cell_Id,TE,TM,ALT,PCI,TAC,RAC,rootSeqIndex,AdminCellState,E_UTRAN_Avg_PRB_usage_per_TTI_DL,E_UTRAN_avg_IP_sched_thp_DL_QCI9,Average_CQI,Avg_UE_distance,distrito,refarming,cambiopcidinamico) 
FROM 'D:\SharkTank\ManagementPlatform\mysite\static\\files\sage_lncel.csv' DELIMITER ',' CSV HEADER;''',
             '''with celdas as ( -- Creates a temporary table called cells with the following query as its data
        select cell_id,lon_site,lat_site,az,bw,RD_normal,
            st_setsrid(st_point(lon_site, lat_site), 4326) as center,
            -- Projects the coordinate in 10_000 meters in the azimuth + (h_beam_width / 2) direction
            st_project( -- Triangle upper point 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                RD_normal*1000, -- Radius in meters
                radians(az - (bw / 2))
            )::geometry as p_upper,
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                RD_normal*1000, 
                radians(az - (bw / 2) + (bw/5))
            )::geometry as p_mid1,	
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                RD_normal*1000, 
                radians(az - (bw / 2)+ (2*bw/5))
            )::geometry as p_mid2,	
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                RD_normal*1000, 
                radians(az - (bw / 2)+ (3*bw/5))
            )::geometry as p_mid3,	
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                RD_normal*1000, 
                radians(az - (bw / 2)+ (4*bw/5))
            )::geometry as p_mid4,
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                RD_normal*1000, 
                radians(az + (bw / 2))
            )::geometry as p_lower
        from sage_lncel
    )
    update sage_lncel SET 
       sector= st_makepolygon( -- Creates a polygon joining the sides of the triangle
            st_makeline( -- Creates the sides of the triangle
                array[
                    center,
                    p_upper,
					p_mid1,
					p_mid2, 
					p_mid3,
					p_mid4,
                    p_lower, center -- Lower side
                ]
            )
        )
	from celdas
	WHERE sage_lncel.cell_id = celdas.cell_id; ''']
    for m in range(len(query)):
        print(query[m])
        c.execute(query[m], vars=None)
        conn.commit()
    conn.close()

    return HttpResponse('ok', content_type='text/plain')


def draw_wcel(request):
    Sage_wcel.objects.all().delete()
    conn = psycopg2.connect(host=host,
                            database=database,
                            user=user,
                            password=pwd,
                            port="5432")

    c = conn.cursor()
    query = ['DELETE FROM sage_wcel where 1=1', ''' COPY sage_wcel(UARFCN,sitename,sitecode,name,LAT_SITE,LON_SITE,AZ,BW,RD,Expr1,BSC_RNC_MME_NAME,RNCId,WbtsId,LcrId,TE,TM,ALT,PriScrCode,LAC,RAC,rootSeqIndex,AdminCellState,WCelState) 
FROM 'D:\SharkTank\ManagementPlatform\mysite\static\\files\sage_wcel.csv' DELIMITER ',' CSV HEADER;''',
             '''with celdas as ( -- Creates a temporary table called cells with the following query as its data
        select lcrid,lon_site,lat_site,az,bw,rd,
            st_setsrid(st_point(lon_site, lat_site), 4326) as center,
            -- Projects the coordinate in 10_000 meters in the azimuth + (h_beam_width / 2) direction
            st_project( -- Triangle upper point 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                rd*1000, -- Radius in meters
                radians(az - (bw / 2))
            )::geometry as p_upper,
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                rd*1000, 
                radians(az - (bw / 2) + (bw/5))
            )::geometry as p_mid1,	
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                rd*1000, 
                radians(az - (bw / 2)+ (2*bw/5))
            )::geometry as p_mid2,	
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                rd*1000, 
                radians(az - (bw / 2)+ (3*bw/5))
            )::geometry as p_mid3,	
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                rd*1000, 
                radians(az - (bw / 2)+ (4*bw/5))
            )::geometry as p_mid4,
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                rd*1000, 
                radians(az + (bw / 2))
            )::geometry as p_lower
        from sage_wcel
    )
    update sage_wcel SET 
       sector= st_makepolygon( -- Creates a polygon joining the sides of the triangle
            st_makeline( -- Creates the sides of the triangle
                array[
                    center, p_upper, -- Upper side
                     p_mid1, -- Frontal 1
					 p_mid2, -- Frontal 2
					 p_mid3, -- Frontal 3
					 p_mid4, -- Frontal 4
					 p_lower, -- Frontal 5
                     center -- Lower side
                ]
            )
        )
	from celdas
	WHERE sage_wcel.lcrid = celdas.lcrid; ''']
    for m in range(len(query)):
        print(query[m])
        c.execute(query[m], vars=None)
        conn.commit()
    conn.close()

    return HttpResponse('ok', content_type='text/plain')


def draw_bts(request):
    Sage_lncel.objects.all().delete()
    conn = psycopg2.connect(host=host,
                            database=database,
                            user=user,
                            password=pwd,
                            port="5432")

    c = conn.cursor()
    query = ['DELETE FROM sage_wcel', ''' COPY sage_bts(band,cellname,lat_site,lon_site,az,bw,rd,cell_id,bscid,bsc_name,bcfid,btsid,trxid,initialfreq,preferredbcch,status,hoppingSequenceNumber1,bsIdentityCodeBCC,
bsIdentityCodeNCC,bts_state,trx_state,LAC,rac,Refarming) 
FROM 'D:\SharkTank\ManagementPlatform\mysite\static\\files\sage_bts.csv' DELIMITER ',' CSV HEADER;''',
             '''with celdas as ( -- Creates a temporary table called cells with the following query as its data
        select cell_id,lon_site,lat_site,az,bw,rd,
            st_setsrid(st_point(lon_site, lat_site), 4326) as center,
            -- Projects the coordinate in 10_000 meters in the azimuth + (h_beam_width / 2) direction
            st_project( -- Triangle upper point 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                rd*1000, -- Radius in meters
                radians(az - (bw / 2))
            )::geometry as p_upper,
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                rd*1000, 
                radians(az - (bw / 2) + (bw/5))
            )::geometry as p_mid1,	
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                rd*1000, 
                radians(az - (bw / 2)+ (2*bw/5))
            )::geometry as p_mid2,	
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                rd*1000, 
                radians(az - (bw / 2)+ (3*bw/5))
            )::geometry as p_mid3,	
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                rd*1000, 
                radians(az - (bw / 2)+ (4*bw/5))
            )::geometry as p_mid4,
            st_project( 
                st_setsrid(st_point(lon_site, lat_site), 4326),
                rd*1000, 
                radians(az + (bw / 2))
            )::geometry as p_lower
        from sage_bts
    )
    update sage_bts SET 
       sector= st_makepolygon( -- Creates a polygon joining the sides of the triangle
            st_makeline( -- Creates the sides of the triangle
                array[
                    center, p_upper, -- Upper side
                    p_upper, p_mid1, -- Frontal 1
					p_mid1, p_mid2, -- Frontal 2
					p_mid2, p_mid3, -- Frontal 3
					p_mid3, p_mid4, -- Frontal 4
					p_mid4, p_lower, -- Frontal 5
                    p_lower, center -- Lower side
                ]
            )
        )
	from celdas
	WHERE sage_bts.cell_id = celdas.cell_id; ''']
    for m in range(len(query)):
        print(query[m])
        c.execute(query[m], vars=None)
        conn.commit()
    conn.close()

    return HttpResponse('ok', content_type='text/plain')


def draw_2gta(request):
    conn = psycopg2.connect(host=host,
                            database=database,
                            user=user,
                            password=pwd,
                            port="5432")

    c = conn.cursor()
    query = ['DROP TABLE IF EXISTS sage_2gta;',
             ''' CREATE TABLE sage_2gta ( id serial NOT NULL, PERIOD_START_TIME	TEXT	, BSC_name	TEXT	, BCF_name	TEXT	, BTS_name	TEXT	, TA0	int	, TA1	int	, TA2	int	, TA3	int	, TA4	int	, TA5	int	, TA6	int	, TA7	int	, TA8	int	, TA9	int	, TA10	int	, TA11	int	, TA12	int	, TA13	int	, TA14	int	, TA15	int	, TA16	int	, TA17	int	, TA18	int	, TA19	int	, TA20	int	, TA21	int	, TA22	int	, TA23	int	, TA24	int	, TA25	int	, TA26	int	, TA27	int	, TA28	int	, TA29	int	, TA30	int	, TA31	int	, TA32	int	, TA33	int	, TA34	int	, TA35	int	, TA36	int	, TA37	int	, TA38	int	, TA39	int	, TA40	int	, TA41	int	, TA42	int	, TA43	int	, TA44	int	, TA45	int	, TA46	int	, TA47	int	, TA48	int	, TA49	int	, TA50	int	, TA51	int	, TA52	int	, TA53	int	, TA54	int	, TA55	int	, TA56	int	, TA57	int	, TA58	int	, TA59	int	, TA60	int	, TA61	int	, TA62	int	, TA63	
    int);''',
             '''COPY sage_2gta(PERIOD_START_TIME,	BSC_name,	BCF_name,	BTS_name,TA0,	TA1,	TA2,	TA3,	TA4,	TA5,	TA6,	TA7,	TA8,	TA9,	TA10,	TA11,	TA12,	TA13,	TA14,	TA15,	TA16,	TA17,	TA18,	TA19,	TA20,	TA21,	TA22,	TA23,	TA24,	TA25,	TA26,	TA27,	TA28,	TA29,	TA30,	TA31,	TA32,	TA33,	TA34,	TA35,	TA36,	TA37,	TA38,	TA39,	TA40,	TA41,	TA42,	TA43,	TA44,	TA45,	TA46,	TA47,	TA48,	TA49,	TA50,	TA51,	TA52,	TA53,	TA54,	TA55,	TA56,	TA57,	TA58,	TA59,	TA60,	TA61,	TA62,	TA63
) 
FROM 'D:\Proyecto_Visualizacion_PostgreSQL\Timing_Advance_2G\merged\\timing_total_2g.csv' DELIMITER ';' ;''',
             ''' DROP TABLE IF EXISTS sage_2gta_prach; ''',
             '''CREATE TABLE sage_2gta_prach
(
id serial NOT NULL,
dia text,
bts_name text,
bin_TA smallint,
porcentaje float,
cant int,
refarming TEXT,
band smallint,
initialfreq int,
bin_geografico GEOMETRY
); ''', '''


WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('16',abc.bts_name) as bin_geografico,abc.ta16,
	COALESCE(100*(TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63)/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq,	
	abc.TA16+abc.TA17+abc.TA18+abc.TA19+abc.TA20+abc.TA21+abc.TA22+abc.TA23+abc.TA24+abc.TA25+abc.TA26+abc.TA27+abc.TA28+abc.TA29+abc.TA30+abc.TA31+abc.TA32+abc.TA33+abc.TA34+abc.TA35+abc.TA36+abc.TA37+abc.TA38+abc.TA39+abc.TA40+abc.TA41+abc.TA42+abc.TA43+abc.TA44+abc.TA45+abc.TA46+abc.TA47+abc.TA48+abc.TA49+abc.TA50+abc.TA51+abc.TA52+abc.TA53+abc.TA54+abc.TA55+abc.TA56+abc.TA57+abc.TA58+abc.TA59+abc.TA60+abc.TA61+abc.TA62+abc.TA63 as restantes
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta16 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq, restantes
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,16,porcentaje,bin_geografico,restantes,refarming,band,initialfreq FROM bines;


WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('15',abc.bts_name) as bin_geografico,abc.ta15,
	COALESCE(100*ta15/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),1 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta15 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,15,porcentaje,bin_geografico,ta15,refarming,band,initialfreq FROM bines;



WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('14',abc.bts_name) as bin_geografico,abc.ta14,
	COALESCE(100*ta14/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta14 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,14,porcentaje,bin_geografico,ta14,refarming,band,initialfreq FROM bines;




WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('13',abc.bts_name) as bin_geografico,abc.ta13,
	COALESCE(100*ta13/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta13 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,13,porcentaje,bin_geografico,ta13,refarming,band,initialfreq FROM bines;




WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('12',abc.bts_name) as bin_geografico,abc.ta12,
	COALESCE(100*ta12/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta12 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,12,porcentaje,bin_geografico,ta12,refarming,band,initialfreq FROM bines;



WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('11',abc.bts_name) as bin_geografico,abc.ta11,
	COALESCE(100*ta11/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta11 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,11,porcentaje,bin_geografico,ta11,refarming,band,initialfreq FROM bines;




WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('10',abc.bts_name) as bin_geografico,abc.ta10,
	COALESCE(100*ta10/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta10 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,10,porcentaje,bin_geografico,ta10,refarming,band,initialfreq FROM bines;



WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('9',abc.bts_name) as bin_geografico,abc.ta9,
	COALESCE(100*ta9/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta9 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,9,porcentaje,bin_geografico,ta9,refarming,band,initialfreq FROM bines;




WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('8',abc.bts_name) as bin_geografico,abc.ta8,
	COALESCE(100*ta8/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta8 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,8,porcentaje,bin_geografico,ta8,refarming,band,initialfreq FROM bines;



WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('7',abc.bts_name) as bin_geografico,abc.ta7,
	COALESCE(100*ta7/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta7 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,7,porcentaje,bin_geografico,ta7,refarming,band,initialfreq FROM bines;




WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('6',abc.bts_name) as bin_geografico,abc.ta6,
	COALESCE(100*ta6/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta6 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,6,porcentaje,bin_geografico,ta6,refarming,band,initialfreq FROM bines;




WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('5',abc.bts_name) as bin_geografico,abc.ta5,
	COALESCE(100*ta5/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta5 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,5,porcentaje,bin_geografico,ta5,refarming,band,initialfreq FROM bines;




WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('4',abc.bts_name) as bin_geografico,abc.ta4,
	COALESCE(100*ta4/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta4 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,4,porcentaje,bin_geografico,ta4,refarming,band,initialfreq FROM bines;




WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('3',abc.bts_name) as bin_geografico,abc.ta3,
	COALESCE(100*ta3/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta3 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,3,porcentaje,bin_geografico,ta3,refarming,band,initialfreq FROM bines;



WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('2',abc.bts_name) as bin_geografico,abc.ta2,
	COALESCE(100*ta2/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta2 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,2,porcentaje,bin_geografico,ta2,refarming,band,initialfreq FROM bines;



WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('1',abc.bts_name) as bin_geografico,abc.ta1,
	COALESCE(100*ta1/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta1 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,1,porcentaje,bin_geografico,ta1,refarming,band,initialfreq FROM bines;



WITH bines as(
 SELECT abc.period_start_time, abc.bts_name, crear_bin('0',abc.bts_name) as bin_geografico,abc.ta0,
	COALESCE(100*ta0/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	as porcentaje , wtf.refarming, wtf.band , wtf.initialfreq
 	FROM sage_2gta as abc
	INNER JOIN sage_bts as wtf ON wtf.cellname = abc.bts_name
	
	group by abc.period_start_time, abc.bts_name ,bin_geografico,abc.ta0 , porcentaje, wtf.refarming, wtf.band, wtf.initialfreq
	
)
INSERT INTO sage_2gta_prach(dia,bts_name,bin_TA,porcentaje,bin_geografico,cant,refarming,band,initialfreq )
SELECT period_start_time,bts_name,0,porcentaje,bin_geografico,ta0,refarming,band,initialfreq FROM bines;'''

             ]
    for m in range(len(query)):
        print(query[m])
        c.execute(query[m], vars=None)
        conn.commit()
    conn.close()

    return HttpResponse('ok', content_type='text/plain')


def draw_3gta(request):
    conn = psycopg2.connect(host=host,
                            database=database,
                            user=user,
                            password=pwd,
                            port="5432")

    c = conn.cursor()
    query = ['''
    DROP TABLE IF EXISTS sage_3gta;
CREATE TABLE sage_3gta
(
id serial NOT NULL,
PERIOD_START_TIME		TEXT	,
PLMN_name		TEXT	,
RNC_name		TEXT	,
Wname		TEXT	,
WBTS_ID		TEXT	,
name		TEXT	,
WCEL_ID		INT	,
prachconf   SMALLINT,
Prach0		INT	,
Prach1		INT	,
Prach2		INT	,
Prach3		INT	,
Prach4		INT	,
Prach5		INT	,
Prach6		INT	,
Prach7		INT	,
Prach8		INT	,
Prach9		INT	,
Prach10		INT	,
Prach11		INT	,
Prach12		INT	,
Prach13		INT	,
Prach14		INT	,
Prach15		INT	,
Prach16		INT	,
Prach17		INT	,
Prach18		INT	,
Prach19		INT	,
Prach20		INT	,
Prach21		INT	
);


COPY sage_3gta(PERIOD_START_TIME,	PLMN_name,	RNC_name,	Wname,	WBTS_ID,	name,	WCEL_ID,prachconf,	Prach0,	Prach1,	Prach2,	Prach3,	Prach4,	Prach5,	Prach6,	Prach7,	Prach8,	Prach9,	Prach10,	Prach11,	Prach12,	Prach13,	Prach14,	Prach15,	Prach16,	Prach17,	Prach18,	Prach19,	Prach20)
 
FROM 'D:\SharkTank\ManagementPlatform\mysite\static\\files\prach_3g.csv' DELIMITER ',' ;



DROP TABLE IF EXISTS sage_3gta_prach;

CREATE TABLE sage_3gta_prach
(
id serial NOT NULL,
dia text,
name text,
bin_Prach smallint,
porcentaje float,
cant int,
uarfcn smallint,
priscrcode int,
bin_geografico GEOMETRY
);



-- WITH bines as(
 -- SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('16',abc.name) as bin_geografico,abc.ta16,
	-- COALESCE(100*(TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63)/NULLIF(TA0+TA1+TA2+TA3+TA4+TA5+TA6+TA7+TA8+TA9+TA10+TA11+TA12+TA13+TA14+TA15+TA16+TA17+TA18+TA19+TA20+TA21+TA22+TA23+TA24+TA25+TA26+TA27+TA28+TA29+TA30+TA31+TA32+TA33+TA34+TA35+TA36+TA37+TA38+TA39+TA40+TA41+TA42+TA43+TA44+TA45+TA46+TA47+TA48+TA49+TA50+TA51+TA52+TA53+TA54+TA55+TA56+TA57+TA58+TA59+TA60+TA61+TA62+TA63,0),0 )
	-- as porcentaje , wtf.refarming, wtf.uarfcn , wtf.priscrcode,	
	-- abc.TA16+abc.TA17+abc.TA18+abc.TA19+abc.TA20+abc.TA21+abc.TA22+abc.TA23+abc.TA24+abc.TA25+abc.TA26+abc.TA27+abc.TA28+abc.TA29+abc.TA30+abc.TA31+abc.TA32+abc.TA33+abc.TA34+abc.TA35+abc.TA36+abc.TA37+abc.TA38+abc.TA39+abc.TA40+abc.TA41+abc.TA42+abc.TA43+abc.TA44+abc.TA45+abc.TA46+abc.TA47+abc.TA48+abc.TA49+abc.TA50+abc.TA51+abc.TA52+abc.TA53+abc.TA54+abc.TA55+abc.TA56+abc.TA57+abc.TA58+abc.TA59+abc.TA60+abc.TA61+abc.TA62+abc.TA63 as restantes
 	-- FROM sage_3gta as abc
	-- INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	-- group by abc.period_start_time, abc.name ,bin_geografico,abc.ta16 , porcentaje, wtf.refarming, wtf.uarfcn, wtf.priscrcode, restantes
	
-- )
-- INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,refarming,uarfcn,priscrcode )
-- SELECT period_start_time,name,16,porcentaje,bin_geografico,restantes,refarming,uarfcn,priscrcode FROM bines;

WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('19',abc.name) as bin_geografico,
	COALESCE(100*(Prach19+Prach20)/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode,
	Prach19+Prach20 as restantes
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,restantes , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,19,porcentaje,bin_geografico,restantes,uarfcn,priscrcode FROM bines;


WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('18',abc.name) as bin_geografico,abc.Prach18,
	COALESCE(100*Prach18/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach18 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,18,porcentaje,bin_geografico,Prach18,uarfcn,priscrcode FROM bines;


WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('17',abc.name) as bin_geografico,abc.Prach17,
	COALESCE(100*Prach17/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach17 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,17,porcentaje,bin_geografico,Prach17,uarfcn,priscrcode FROM bines;


WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('16',abc.name) as bin_geografico,abc.Prach16,
	COALESCE(100*Prach16/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach16 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,16,porcentaje,bin_geografico,Prach16,uarfcn,priscrcode FROM bines;

WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('15',abc.name) as bin_geografico,abc.Prach15,
	COALESCE(100*Prach15/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach15 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,15,porcentaje,bin_geografico,Prach15,uarfcn,priscrcode FROM bines;

WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('14',abc.name) as bin_geografico,abc.Prach14,
	COALESCE(100*Prach14/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach14 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,14,porcentaje,bin_geografico,Prach14,uarfcn,priscrcode FROM bines;

WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('13',abc.name) as bin_geografico,abc.Prach13,
	COALESCE(100*Prach13/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach13 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,13,porcentaje,bin_geografico,Prach13,uarfcn,priscrcode FROM bines;

WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('12',abc.name) as bin_geografico,abc.Prach12,
	COALESCE(100*Prach12/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach12 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,12,porcentaje,bin_geografico,Prach12,uarfcn,priscrcode FROM bines;


WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('11',abc.name) as bin_geografico,abc.Prach11,
	COALESCE(100*Prach11/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach11 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,11,porcentaje,bin_geografico,Prach11,uarfcn,priscrcode FROM bines;


WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('1',abc.name) as bin_geografico,abc.Prach1,
	COALESCE(100*Prach1/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach1 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,1,porcentaje,bin_geografico,Prach1,uarfcn,priscrcode FROM bines;



WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('10',abc.name) as bin_geografico,abc.Prach10,
	COALESCE(100*Prach10/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach10 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,10,porcentaje,bin_geografico,Prach10,uarfcn,priscrcode FROM bines;


WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('9',abc.name) as bin_geografico,abc.Prach9,
	COALESCE(100*Prach9/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach9 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,9,porcentaje,bin_geografico,Prach9,uarfcn,priscrcode FROM bines;

WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('8',abc.name) as bin_geografico,abc.Prach8,
	COALESCE(100*Prach8/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach8 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,8,porcentaje,bin_geografico,Prach8,uarfcn,priscrcode FROM bines;


WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('7',abc.name) as bin_geografico,abc.Prach7,
	COALESCE(100*Prach7/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach7 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,7,porcentaje,bin_geografico,Prach7,uarfcn,priscrcode FROM bines;

WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('6',abc.name) as bin_geografico,abc.Prach6,
	COALESCE(100*Prach6/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach6 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,6,porcentaje,bin_geografico,Prach6,uarfcn,priscrcode FROM bines;


WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('5',abc.name) as bin_geografico,abc.Prach5,
	COALESCE(100*Prach5/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach5 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,5,porcentaje,bin_geografico,Prach5,uarfcn,priscrcode FROM bines;


WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('4',abc.name) as bin_geografico,abc.Prach4,
	COALESCE(100*Prach4/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach4 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,4,porcentaje,bin_geografico,Prach4,uarfcn,priscrcode FROM bines;

WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('3',abc.name) as bin_geografico,abc.Prach3,
	COALESCE(100*Prach3/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach3 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,3,porcentaje,bin_geografico,Prach3,uarfcn,priscrcode FROM bines;


WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('2',abc.name) as bin_geografico,abc.Prach2,
	COALESCE(100*Prach2/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach2 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,2,porcentaje,bin_geografico,Prach2,uarfcn,priscrcode FROM bines;



WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('1',abc.name) as bin_geografico,abc.Prach1,
	COALESCE(100*Prach1/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach1 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,1,porcentaje,bin_geografico,Prach1,uarfcn,priscrcode FROM bines;


WITH bines as(
 SELECT abc.period_start_time, abc.name, crear_bin_prach3g_v2('0',abc.name) as bin_geografico,abc.Prach0,
	COALESCE(100*Prach0/NULLIF(Prach0+	Prach1+	Prach2+	Prach3+	Prach4+	Prach5+	Prach6+	Prach7+	Prach8+	Prach9+	Prach10+	Prach11+	Prach12+	Prach13+	Prach14+	Prach15+	Prach16+	Prach17+	Prach18+	Prach19+	Prach20,0),1 )
	as porcentaje , wtf.uarfcn , wtf.priscrcode
 	FROM sage_3gta as abc
	INNER JOIN sage_wcel as wtf ON wtf.name = abc.name
	
	group by abc.period_start_time, abc.name ,bin_geografico,abc.Prach0 , porcentaje, wtf.uarfcn, wtf.priscrcode
	
)
INSERT INTO sage_3gta_prach(dia,name,bin_Prach,porcentaje,bin_geografico,cant,uarfcn,priscrcode )
SELECT period_start_time,name,0,porcentaje,bin_geografico,Prach0,uarfcn,priscrcode FROM bines;


    
     ''']
    for m in range(len(query)):
        print(query[m])
        c.execute(query[m], vars=None)
        conn.commit()
    conn.close()

    return HttpResponse('ok', content_type='text/plain')
