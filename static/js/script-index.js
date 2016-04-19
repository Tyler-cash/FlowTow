/**
 * Created by tyler on 17/04/2016.
 */

$(document).ready(function () {
    var url = window.location.pathname;
    if (url === "/about") {
        $("#nav-about").addClass("active");
    } else if (url === "/") {
        $("#nav-home").addClass("active");
    } else if (url === "/profile") {
        $("#nav-profile").addClass("active");
    }


    $('form').click(function () {
        $(this).submit();
        return false;
    });
});

