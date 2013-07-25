$(function(){
    $('#quick-search-btn').click(function(e){
        var crn = $('#crn-input').val();
        if(!crn){
            crn=0; 
        }
        var term = $('#term-input').val();
        var url = "/seats_check/" + crn;
        term = encodeURIComponent(term)
        $.ajaxSetup({async: false});
        $.get(url, {'term':term}, function(data){
            if(data['code'] == 0){
                $('.result-error').text(data['content']);
                $('.result').hide();
                $('.result-error').show();
                $('#save').addClass('disabled');
                $('#save').attr('disabled','disabled');
            }else{
                var content = data['content']; 
                $('#inputMax').text(content['max_num']);
                $('#inputCur').text(content['curr_num']);
                $('#inputRem').text(content['rem_num']);
                $('#inputName').text(content['name']);
                $('#inputCode').text(content['code']);
                $('#inputNum').text(content['number']);
                $('.result').show();
                $('.result-error').hide();
                $('#save').removeClass('disabled');
                $('#save').removeAttr('disabled');
            }
        });
    });
    $('#save').click(function(e){
        $("#add-sec").submit();
    });
});

