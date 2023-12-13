let hijack = true

function success(position){
    var lat, lng;
    if (hijack){
        var waypts = routeCtrl.getWaypoints();
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
            "lat": lat,
            "lng": lng,
        },
        headers:{
            "X-CSRFToken": '{{ csrf_token }}'
        },
        success: function (data) {
            //alert("successfull")
        },
        failure: function () {
            //alert("failure");
        }
    });
    console.log(lat);
    console.log(lng);
        // sessionStorage.setItem("user_lat", lat);
        // sessionStorage.setItem("user_lng", lng);
}

function error(position){
    console.log(error) 
}
// options -> high acuracy
let id = navigator.geolocation.watchPosition(success, error);