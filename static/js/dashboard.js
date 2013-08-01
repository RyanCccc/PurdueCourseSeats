$(function() {
    var shown = false;
    function showIFrame(obj) {
        obj.animate({
            'left': '10%'
        }, 400);
        shown = true;
    }

    function hideIFrame() {
        $('.iframe').animate({
            'left': '100%'
        }, 400);
        shown = false;
    }

    $('.send-restrict-checkbox').click(function() {
        if($(this).prop('checked')){
            $('.send-restrict-checkbox').prop('checked',true);
        }else{
            $('.send-restrict-checkbox').prop('checked',false);
        }
    });

    $('.if-btn').click(function() {
        $iframe = $('#' + $(this).attr('for'));
        if (!$iframe.attr('src')) {
            $iframe.attr('src', $(this).attr('src'));
        }
        if (!shown) {
            $(document).on('click', 'body', hideIFrame);
            showIFrame($iframe);
        } else {
            $(document).off('click', 'body', hideIFrame);
            hideIFrame();
        }
        return false;
    });
});
