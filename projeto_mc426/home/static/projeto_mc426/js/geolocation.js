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