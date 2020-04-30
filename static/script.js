$('td:contains("None")').each(function () {
    $(this).html($(this).html().split("None").join(""));
});

$(document).ready(function () {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function () {

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");

    });

    var length = $(".field.has-addons").length
    if (length > 1) {
        $(".field.has-addons:first").remove()
    }
    $("#enter").click(function () {
        $("#link").parent().addClass("is-loading")
        if(!$("#link").val())
            window.location = "/watch?url=" + "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        else
            window.location = "/watch?url=" + $("#link").val()
    })

});

