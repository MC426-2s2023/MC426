function getPolygons(crimeData, L){
    var list = [];
    var dist = 0.00015;
    var ocurr = crimeData.data;
    for (const i in ocurr){
        var pol = [];
        //L.marker([ocurr[i].lat, ocurr[i].lng]).addTo(map);

        pol.push([ocurr[i].lng - dist, ocurr[i].lat - dist]);
        //L.marker([ocurr[i].lat + dist, ocurr[i].lng - dist]).addTo(map);

        pol.push([ocurr[i].lng - dist, ocurr[i].lat + dist]);
        //L.marker([ocurr[i].lat - dist, ocurr[i].lng - dist]).addTo(map);

        pol.push([ocurr[i].lng + dist, ocurr[i].lat + dist]);
        //L.marker([ocurr[i].lat - dist, ocurr[i].lng + dist]).addTo(map);

        pol.push([ocurr[i].lng + dist, ocurr[i].lat - dist]);
        //L.marker([ocurr[i].lat + dist, ocurr[i].lng + dist]).addTo(map);

        pol.push([ocurr[i].lng - dist, ocurr[i].lat - dist]);
        //L.marker([ocurr[i].lat + dist, ocurr[i].lng - dist]).addTo(map);
        list.push([pol]);
    }
    return list;
}


const apikey = "5b3ce3597851110001cf62483b054b57335d4a5a8ccfbf5ebdf23f1e";
const osrRouter = new L.Routing.OpenRouteService(apikey, {
        "timeout": 30 * 1000, // 30",
        "format": "json",                           // default, gpx not yet supported
        "host": "https://api.openrouteservice.org", // default if not setting
        "service": "directions",                    // default (for routing) 
        "api_version": "v2",                        // default
        "profile": "cycling-road",                  // default
        "routingQueryParams": {
            "attributes": [
                "avgspeed",
                "percentage"
            ],
            "language": "pt-pt",
            "maneuvers": "true",
            "preference": "recommended",
          "options": {
              "avoid_polygons": {
                  "type": "MultiPolygon",
                  "coordinates": getPolygons(data, L)
                 }
            }
        }
});

var routeCtrl = L.Routing.control({
    router: osrRouter,
    waypoints: [
        L.latLng(-22.82578415192047, -47.072228935407814),
        L.latLng(-22.82384289829194, -47.07019292913905)
    ]
}).addTo(map);

