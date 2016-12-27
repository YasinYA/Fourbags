$(document).ready(function() {
    var scrollStart = 0;
    var startChanging = $('.content_wrapper');
    var coordinates = startChanging.offset();

    if (startChanging.length) {
        $(document).scroll(function() {
            scrollStart = $(this).scrollTop();
            if(scrollStart > coordinates.top) {
                $('.navbar-default').css('background', '#37474f');
            } else {
                $('.navbar-default').css('background', 'transparent');
            }
        });
    }

});
