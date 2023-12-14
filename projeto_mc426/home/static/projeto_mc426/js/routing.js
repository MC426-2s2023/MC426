function getPolygons(crimeData, L){
    var list = [];
    var dist = 0.0002;
    var ocurr = crimeData.data;
    for (const i in ocurr){
        var pol = [];
        //L.marker([ocurr[i].lat, ocurr[i].lng]).addTo(map);

        pol.push([ocurr[i].lng - dist, ocurr[i].lat - dist]);
        //L.marker([ocurr[i].lat + dist, ocurr[i].lng - dist]).addTo(map);

        pol.push([ocurr[i].lng - dist, ocurr[i].lat + dist]);
        //pol.push([ocurr[i].lng + dist, ocurr[i].lat - dist]);
        //L.marker([ocurr[i].lat - dist, ocurr[i].lng - dist]).addTo(map);

        pol.push([ocurr[i].lng + dist, ocurr[i].lat + dist]);
        //L.marker([ocurr[i].lat - dist, ocurr[i].lng + dist]).addTo(map);

        pol.push([ocurr[i].lng + dist, ocurr[i].lat - dist]);
        //L.marker([ocurr[i].lat + dist, ocurr[i].lng + dist]).addTo(map);

        pol.push([ocurr[i].lng - dist, ocurr[i].lat - dist]);
        //L.marker([ocurr[i].lat + dist, ocurr[i].lng - dist]).addTo(map);
        list.push([pol]);
    }
    console.log(list)
    return list;
}

const apikey = "5b3ce3597851110001cf62483b054b57335d4a5a8ccfbf5ebdf23f1e";
const osrRouter = new L.Routing.OpenRouteService(apikey, {
        "timeout": 30 * 1000, // 30",
        "format": "json",                           // default, gpx not yet supported
        "host": "https://api.openrouteservice.org", // default if not setting
        "service": "directions",                    // default (for routing) 
        "api_version": "v2",                        // default
        "profile": "driving-car" ,
        // "profiles": {
        //     "active": [
        //         "car"
        //       ],
        //     // "inactive": [
        //     //     "walking"
        //     // ]
        // },
        
        //"driving-car",                  // default
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
    //waypoints: [
    //    L.latLng(-22.82578415192047, -47.072228935407814),
    //    L.latLng(-22.82384289829194, -47.07019292913905)
    //],
    language: 'pt',
    collapsible: true,
    //geocoder: L.Control.Geocoder.nominatim(),
}).addTo(map);

routeCtrl.hide();

function createButton(label, container) {
    var btn = L.DomUtil.create('button', '', container);
    btn.setAttribute('type', 'button');
    btn.innerHTML = label;
    return btn;
}

map.on('click', function(e) {
    var container = L.DomUtil.create('div'),
        startBtn = createButton('Origem', container),
        destBtn = createButton('Destino', container);

    L.popup()
        .setContent(container)
        .setLatLng(e.latlng)
        .openOn(map);

    L.DomEvent.on(startBtn, 'click', function() {
        routeCtrl.spliceWaypoints(0, 1, e.latlng);
        map.closePopup();
    });
        
    L.DomEvent.on(destBtn, 'click', function() {
        routeCtrl.spliceWaypoints(routeCtrl.getWaypoints().length - 1, 1, e.latlng);
        map.closePopup();
    });
});



function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }
 
let hijack = true;

function success(position){
    var lat, lng;
    var waypts = routeCtrl.getWaypoints();
    //console.log(waypts[0].latLng)
    if (hijack && typeof waypts[0].latLng !== "undefined"){
        lat = (waypts[0].latLng.lat);
        lng = (waypts[0].latLng.lng);
    } else {
        lat = position.coords.latitude;
        lng = position.coords.longitude;
    }
    var csrf = $(this).attr('csrf');
    $.ajax({
        type: "POST",
        url: '/home/update_user_location/',
        data: {
            //csrfmiddlewaretoken: '{{ csrf_token }}',           
            "lat": lat,
            "lng": lng,
        },
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        success: function (data) {
            //alert("successfull")
        },
        failure: function () {
            //alert("failure");
        }
    });
    //console.log(routeCtrl);
    //console.log(lat);
    //console.log(lng);
        // sessionStorage.setItem("user_lat", lat);
        // sessionStorage.setItem("user_lng", lng);
}

function error(position){
    console.log(error) 
}
// options -> high acuracy
let id = navigator.geolocation.watchPosition(success, error);
