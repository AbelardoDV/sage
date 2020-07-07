from django.shortcuts import render
from django.http import HttpResponse
from .models import Webcell4G
import psycopg2
# Create your views here.

host = "localhost"
database = "Practicando"
user = "postgres"
pwd = "nemuuser"

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def crear_4g_view(request):
    Webcell4G.objects.using('spatial').all().delete()
    conn = psycopg2.connect(host=host,
                            database=database,
                            user=user,
                            password=pwd,
                            port="5432")
            



    c = conn.cursor()
    query = [''' COPY webcell_4g(DL_CH,SiteName,CellName,LAT_SITE,LON_SITE,AZ,BW,RD,RD_normal,separar,MME,MME_ID,lnBtsId,Cell_Id,TE,TM,ALT,PCI,TAC,RAC,rootSeqIndex,AdminCellState,E_UTRAN_Avg_PRB_usage_per_TTI_DL,E_UTRAN_avg_IP_sched_thp_DL_QCI9,Average_CQI,Avg_UE_distance,distrito,refarming) 
FROM 'D:\Proyecto_Visualizacion_PostgreSQL\WebCell_4G.csv' DELIMITER ',' CSV HEADER;''', '''with celdas as ( -- Creates a temporary table called cells with the following query as its data
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
        from webcell_4g
    )
    update webcell_4g SET 
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
	WHERE webcell_4g.cell_id = celdas.cell_id; ''']
    for m in range(len(query)):
        print(query[m])
        c.execute(query[m], vars=None)
        conn.commit()
    conn.close()

    return HttpResponse('ok', content_type='text/plain')
