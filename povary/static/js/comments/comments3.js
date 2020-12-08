/**
 * selectors
 *   toggle : открывает блок с формой
 *   block : куда вставлять добавленный комментарий
 *   form :  форма для ввода 
 *   parent:  блок комментария
 *   ---------------
 *   notEmpty  - список непустых полей (валидация до отправки на сервер)
 *   [["selector", "сообщение"], ["selector", "сообщение"]....]    
 *   -------------
 *   isEnd - куда добавлять дынные в конец или начало блока, 
 *    true в конец по умолчанию, false - в начало 
 *   -------------- 
 *   Использование 
 *   var commentsReply = new CommentsReply(selectors, template, isEnd);  
 *    commentsReply.init(); 
 *     
**/
function CommentsReply (selectors, notEmpty, isEnd) { 
	var default_selectors = { form : ".answer_form",
		toggle : "a.commentanswer_link",
		block : ".comment_answers",
		parent : ".article_comment"
	};  
	var default_notEmpty = {}; 
	this.isEnd = isEnd && true; 
	if (typeof selectors == 'object') {
		this.selectors = $.extend(default_selectors, selectors);
	} else {
		this.selectors = default_selectors;
	}
	delete default_selectors;   
	if (typeof notEmpty == 'object') {
		 this.notEmpty = $.extend(true, [], notEmpty);
	} else {
		 this.notEmpty = [];
	}    
	var self = this;
	
	this.init = function () { 
		$(self.selectors.toggle).text("Ответить на комментарий");        
		$(self.selectors.form).on("submit", self.send); 
		$(self.selectors.toggle).on("click", self.toggleForm);       
	}
	this.send = function(event) {
	event.preventDefault(); 
		event.stopPropagation(); 
		var parent = $(this).parents(self.selectors.parent);
		var length = self.notEmpty.length;
		var emptyMsg = '';
		for (var i=0; i<length; i++ ) {
			if ( $(this).find(self.notEmpty[i][0]).val() == "" ) {
				emptyMsg += self.notEmpty[i][1]; 
			}
		}
		if (emptyMsg.length > 0) {
		  alert(emptyMsg);
		  return false;
		} 
		// подготовка формы к отправке
		//$(this).find('input[type=file]').val(''); // проверить обнуление файлов 
		var form_data = $(this).serializeArray();
		var form_url = $(this).attr("action");
		$.ajax ({             
			url: form_url,
			type: "POST",
			data: form_data,              
			dataType: "json",
			timeout: 30000,
			success: function(data){
				if (data.status == 'error' || data.status == "validation_error"){
					alert(data.message);
				}
				else{	//console.log(data);
					   //var html = self._render(data);
					   var html = data.data; //console.log(html);
					   if (self.isEnd) {
						  $($(html)).appendTo($(parent).find(self.selectors.block));
						} else {
						   $($(html)).prependTo($(parent).find(self.selectors.block));
						}
					   $(parent).find(self.selectors.toggle).remove();
					   $(parent).find(self.selectors.form).remove();
				}
			},
			error: function(x, text, th) {
				//console.log(text);
				alert('Время ожидания истекло!');
			}
		});
		// отправка данных формы на сервер
		return false;
	}
	this.toggleForm = function(event) {
		event.preventDefault(); 
		event.stopPropagation();
		var parent = $(this).parents(self.selectors.parent);
		var text = $(this).text();
		if (text == "Ответить на комментарий") {
			$(this).text("Скрыть форму ответа");
			$(parent).find(self.selectors.form).show();
		} else {
			$(this).text("Ответить на комментарий");
			$(parent).find(self.selectors.form).hide();
		}  
	}

}
$(function(){  
	var commentReply = new CommentsReply( null, [["textarea", "текст ответа на комментарий не должен быть пуст!"]], false);
	commentReply.init();
	});
  




