L.Control.Overview = L.Control.extend({
  options: {
    position: 'bottomright',
  },
  
  // In order to keep the overview map in sync with the main map, each layer
  // must have a 'name' attribute
  // 
  // e.g. var osm = L.tileLayer('http://...', name: 'osm', attribution: ...)
  initialize: function(layers) {
    this._layers = layers;
    this._currentBaseLayer = layers[0];
  },
  
  onAdd: function(map) {
    this._map = map;
    this._initLayout();
    this._update();
        
    map.on('moveend', this._update, this);
    
    return this._container;
  },
  
  onRemove: function(map) {
    map.off('moveend', this._update, this);
  },
  
  _initLayout: function() {
    var container = this._container = L.DomUtil.create('div', 'leaflet-control-overview'), 
        mapDiv    = L.DomUtil.create('div', 'leaflet-control-overview-map', container);
    
    var overview = this._overview = new L.Map(mapDiv, {
      layers:             [this._currentBaseLayer],
      dragging:           false,
      touchZoom:          false,
      scrollWheelZoom:    false,
      doubleClickZoom:    false,
      boxZoom:            false,
      zoomControl:        false,
      attributionControl: false
    });
    
    var rectangle = this._rectangle = new L.Rectangle(this._map.getBounds(), {weight: 2, clickable: false, color: '#4183c4'});
    overview.addLayer(rectangle);
      
    setTimeout(function() { overview.invalidateSize(); });  // hack
  },
  
  _update: function() {
    var center = this._map.getCenter(), zoom = Math.max(this._map.getZoom() - 4, 0);
    this._overview.setView(center, zoom);
    this._rectangle.setBounds(this._map.getBounds());
  },
});

L.control.overview = function(layer, options) {
  return new L.Control.Overview(layer, options);
};