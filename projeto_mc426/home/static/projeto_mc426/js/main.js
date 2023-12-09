var data = {
    max: 10,
    min: 0,
    data: crimeData
};

// Map base layer
var baseLayer = L.tileLayer(
  'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
  }
);

var cfg = {
    "radius": 0.0005,
    "maxOpacity": .8,
    "minOpacity": 0, 
    // scales the radius based on map zoom
    "scaleRadius": true, 
    // if set to false the heatmap uses the global maximum for colorization
    // if activated: uses the data maximum within the current map boundaries 
    //   (there will always be a red spot with useLocalExtremas true)
    "useLocalExtrema": false,
    // which field name in your data represents the latitude - default "lat"
    latField: 'lat',
    // which field name in your data represents the longitude - default "lng"
    lngField: 'lng',
    // which field name in your data represents the data value - default "value"
    valueField: 'count'
  };

var heatmapLayer = new HeatmapOverlay(cfg)

// Map configuration
var map = new L.Map('map', {
    center: new L.LatLng(-22.817168, -47.069791),
    zoom: 15,
    layers: [baseLayer, heatmapLayer]
  });

heatmapLayer.setData(data);

layer = heatmapLayer;