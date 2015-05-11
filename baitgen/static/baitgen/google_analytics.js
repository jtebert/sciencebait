$(document).ready(function () {
    $(".listing th a").hover(function () {
        //$(this).prepend("<i class='fa fa-link'></i>")
        $(this).children().append('<i class="fa fa-link"></i>');
    }, function () {
        $(this).children().children("i").remove();
    });
});