;$(function(){
	var rankElem = new RankingItem([[".num-like", '.num-liked'], [".like", '.liked']]);
	rankElem.init();
});
function RankingItem (objects) {
	this.objects = $.extend(true, [], objects);
	var self = this; console.log(this.objects);

	this.init = function () {
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
		//array
		$.each(self.objects, self.handler);
	}
	
	this.handler = function(idx, object){
		$(object[0]).on('click.rankingspace', function(event) {
			event.preventDefault();
			var a = this;
			a_href = $(a).attr('href');
			$.ajax({
				url: a_href,
				type: "post",
				dataType: "json",
				success: function(data){ console.log(data);
					if (data.status == 'error' || data.status == "validation_error"){
						console.log(data.message);
					} else { 
						$(a).html(data.votes);//
						var trg1 = object[0];
						trg1 = trg1.replace(/\./gi, '');
						trg1 = trg1.replace(/#/gi, '');
						var trg2 = object[1];
						trg2 = trg2.replace(/\./gi, '');
						trg2 = trg2.replace(/#/gi, '');
						$(a).removeClass(trg1).addClass(trg2);
						$(a).off('click.rankingspace');
						$(a).on('click', self.stopLink);
					}
				},
				error: function(x, text, th) {
					console.log(text);
				}
			});  
			return false;
		});
		$(object[1]).on('click', self.stopLink);
	}
	this.stopLink = function(event) {
		event.preventDefault(); console.log("there");
		return false;
	}
}

