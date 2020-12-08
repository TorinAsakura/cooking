$(function(){
	$("#hide_answers").live("click", function(evnt){
		evnt.preventDefault();
		var answers = $(this).nextAll('#comment_answers').first();
		var _this = $(this);
		answers.toggle('slow', function(){
			if (answers.is(":visible")){
				_this.text("Скрыть ответы");
			}
			else{
				_this.text("Показать ответы");	
			}
		});
	});

	$("#comment form").live('submit', function(evnt){
		evnt.preventDefault();
		var form = $(this);
		var comment_body = $(this).find("textarea[name='body']").val();
		if ( comment_body == ""){
			alert("Вы не можете отправить пустой ответ");
			return;
		}
		form_data = $(this).serializeArray();
		form_url = $(this).attr('action');
		$.post(form_url, form_data, function(data){
			if (data.status == 'error' || data.status == "validation_error"){
				console.log(data.message);
			}
			else{
				// var answer = $("<li></li>");
				// answer.attr("data-id", data.id);
				form.next("#comment_answers").prepend(data);

				// var body_element = $("<p></p>");
				// body_element.html(data.body);
				// body_element.appendTo(answer);

				form.each(function(){
    				this.reset();
 				});
			}
		});
		form.toggle();
		form.prev('#commentanswer_link').text("Ответить на комментарий");
	});
	$("#commentanswer_link").live('click', function(evnt){
		evnt.preventDefault();
		$(this).next("form").toggle();
		$(this).text("Скрыть форму ответа");
	});

    // using jQuery
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

    // Variable to store your files
    var files;

    // Add events
    $('input[type=file]').on('change', prepareUpload);

    // Grab the files and set them to our variable
    function prepareUpload(event)
    {
      files = event.target.files;
    }

	$("#add_comment_form").on('submit', function(evnt){
		console.log("add_comment_form submitted");
		evnt.preventDefault();
        evnt.stopImmediatePropagation();
		/*
		var comment_body = tinyMCE.activeEditor.getContent();
		if ( comment_body == ""){
			alert("Вы не можете отправить пустой комментарий");
			return;
		}
		$("#add_comment_form").find("textarea[name='body']").val(comment_body);
		*/
		var form_data = new FormData($(this)[0]); //$(this).serializeArray()
		var form_url = $(this).attr('data-url');

        if (files){
            $.each(files, function(key, value)
            {
                form_data.append(key,value);
            });
        }

        console.log(files);

		$.ajax ({
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            url: form_url,
            type: "POST",
            data: form_data,
            contentType: false,
            processData: false,
            dataType: "json",
            success: function(data){
                if (data.status == 'error' || data.status == "validation_error"){
                    console.log(data.message);
                }
                else{
                    $("#comments").append(data.data);
                    var comm_caption = data.comm_caption;
                    $("#comm-title").html(comm_caption);
                    var updNum = parseInt($("#num_comments").text())+1;
                    $('.num_comments').each(function(index){$(this).text(updNum);})
                    // reset form fields
                    $('#add_comment_form').each(function(){
                            this.reset();
                    });
                }
            }
        });
	});

	$("#add_answer_form").live('submit', function(evnt){
		var form = $(this);		
		evnt.preventDefault();
        $(".add-commen").toggle();
        var global_activated = ($(".add-commen").attr("activated") === 'True');
        if (global_activated){
            $(".global_comment").toggle();
            $(".add-commen"). text("Скрыть форму коментария");
            $(".textarea-com").focus();
        }
		//
		form_data = $(this).serializeArray();
		form_url = $(this).attr('data-url');
		comment_id = $(this).attr('comment-id');		
		$.post(form_url, form_data, function(data){
			if (data.status == 'error' || data.status == "validation_error"){
				console.log(data.message);
			}
			else{				
				$(".ansver[comment_id='"+comment_id+"']").parent().append(data.data);				
				$(".ansver[comment_id='"+comment_id+"']").attr("active","false");						
				var comm_caption = data.comm_caption;				
				$("#comm-title").html(comm_caption);
				var updNum = parseInt($("#num_comments").text())+1;
				$('.num_comments').each(function(index){$(this).text(updNum);})
				$('#add_answer').hide();
				// reset form fields
				$('#add_answer_form').each(function(){
    					this.reset();
 				});
			}
		});
	});

	$(".c-date").each(function(index){
		var c_date = $(this).html();	
		//$(this).html(moment(c_date).daysInMonth());
	});
	$(".ansver").live('click', function(evnt){	
		var comment_id = $(this).attr("comment_id");
		var form_div = $("#add_answer");
		var form = $("#add_answer_form");
		var activated = ($(this).attr("activated") === 'true');
        var global_activated = ($(".add-commen").attr("activated") === 'True');
        $(".add-commen").toggle();
		if(activated){
			evnt.preventDefault();
			form_div.hide();

            if (global_activated){
                $(".global_comment").toggle();
                $(".add-commen"). text("Скрыть форму коментария");
                $(".textarea-com").focus();
            }
		}else{
			var url = form.attr("data-url-origin");
			url = url.slice(0,-2) + comment_id + "/True";
			form.attr("data-url", url) ;
			form.attr("comment-id", comment_id);
			$(this).parent().append(form_div);
			form_div.show();
            if (global_activated){
                $(".global_comment").toggle();
            }
		}
		$(this).attr("activated", !activated);
	});
	$(".comm-text").live('click', function(evnt){
		evnt.preventDefault();
	});
});

$("#add_answer").hide();

$("#answer_form_submit").live('click', function(evnt){
		evnt.preventDefault();
        $('#answer_form').submit();
	});


