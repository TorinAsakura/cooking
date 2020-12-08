$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});

$(function(){

    fun = function(evnt){            
            var form = $(this);
            evnt.preventDefault();
            form_url = $(this).attr('href');
            $.get(form_url, function(data){            
                if (data.status == 'error' || data.status == "validation_error"){
                    alert(data.message);
                }
                else{
                    $("#ajax_res").html(data);                
                }
            });
        };
    
	$.each($(".cake_mc_filter"), function(i,val){ 
        $(val).off("click").on("click",fun);
	});

    $.each($(".choose"), function(i,val){ 
        $(val).removeClass('active');                
        if($(val).attr('cat')==cat || $(val).attr('ing')==ing)
            $(val).addClass('active');
        if(!(cat=='' && ing==''))
            $("#search_form").find("input").val('');         
    });    
	
});



