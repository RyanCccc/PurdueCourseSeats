$(".banner").click(function(e){
    var data = $("#banner-data");
    if (data.hasClass('in')){
        data.removeClass('in'); 
    }else{
        data.addClass('in');
    }
});
