shown = false;
$(function(){
    $(".if-btn").click(function(){
        if (!shown){
            $(document).on('click','body', hideIFrame);
            showIFrame($('#'+$(this).attr('for')));
        }else{
            $(document).off('click','body', hideIFrame);
            hideIFrame();
        }
        return false;
    });
});

function showIFrame(obj){
    console.log(obj);
    obj.animate({'left':'10%'}, 400);
    shown=true;
}

function hideIFrame(){
    $('.iframe').animate({'left':'100%'}, 400);
    shown=false;
}
