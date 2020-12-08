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

$(".num-liked, .liked").live('click', function(evnt){
	evnt.preventDefault();
		var a = $(this);	
		a_href = a.attr('href');	
		$.ajax({
		  url: a_href,
		  type: "post",                 
		}).done(function(data) {
			if (data.status == 'error' || data.status == "validation_error"){
				console.log(data.message);
			}
			else{
				a.html(data.votes);
				if(a.hasClass('num-liked')){
					a.toggleClass('num-liked num-like');
				}
				if(a.hasClass('liked')){
					a.toggleClass('liked like');
				}
				//alert(data.message);
			}
		});	
});


	$(".num-like, .like").live('click', function(evnt){
		evnt.preventDefault();
		var a = $(this);	
		a_href = a.attr('href');	
		$.ajax({
		  url: a_href,
		  type: "post",                 
		}).done(function(data) {
			if (data.status == 'error' || data.status == "validation_error"){
				console.log(data.message);
			}
			else{
				a.html(data.votes);
				if(a.hasClass('num-like')){
					a.toggleClass('num-like num-liked');
				}
				if(a.hasClass('like')){
					a.toggleClass('like liked');
				}
				//alert(data.message);
			}
		});		
	});

	
