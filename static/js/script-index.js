/**
 * Created by tyler on 17/04/2016.
 */

$(document).ready(function () {
    var url = window.location.pathname;
    if (url === "/about") {
        $("#nav-about").addClass("active");
    } else if (url === "/") {
        $("#nav-home").addClass("active");
    } else if (url === "/my") {
        $("#nav-profile").addClass("active");
    }
});

