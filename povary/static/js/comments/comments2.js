/**
 * selectors
 *   block : общий блок с формой и прочим
  *  form :  форма с комментарием
 *   img_block :  где будет появляться превью загружаемой картинки
 *   msg_block :  сообщения об ошибках
 *   comments_block:  блок, куда вставлять свежедобавленные комментарии
 *   -------------------------------------------  
 *   notEmpty  - список непустых полей (валидация до отправки на сервер)
 *   [["selector", "сообщение"], ["selector", "сообщение"]....] 
 *   -------------------------------------------- 
 *   Использование 
 *   var commentsBlock = new CommentsRule(selectors,  notEmpty);  
 *    commentsBlock.init(); 
 *     
**/
function CommentsRule (selectors, notEmpty) { 
	var default_selectors = { block : ".registr-center",
		form : "#add_comment_form",
		img_block : ".r-img",
		msg_block : ".msg_block",
		comments_block : "#comments"
	}; 
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
		$(self.selectors.form).on("submit", self.sendForm);
		if(window.File && window.FileReader && window.FileList && window.Blob) { 
			$(self.selectors.form).find('input[type=file]').on('change', self.fileInsert);
		}
	}
	this.sendForm = function(event) { 
		if (typeof $(this).attr("target") == "undefined") { 
			event.preventDefault(); 
			event.stopPropagation(); 
			if (! self._formValidation(this)) return false;
			var isFiles = self._checkFiles(this); 
			if ((! isFiles) || (window.FormData)) {
				var parent = $(this).parents(self.selectors.block);
				if(! isFiles) {
					var form_data = $(this).serializeArray();
					var prData = true;
					var cntType = 'application/x-www-form-urlencoded; charset=UTF-8';
				} else {
					var form_data = new FormData(this);
					var prData = false;
					var cntType = false;
				}
				var form_url = $(this).attr("data-url");
				$.ajax ({  
					headers: { "X-CSRFToken": self.getCookie("csrftoken") },
					url: form_url,
					type: "POST",
					processData: prData,  
					contentType: cntType,
					data: form_data,              
					dataType: "json",
					success: function(data){
						self._dataRender(data, parent);
					},
					error: function(x, text, th) {
						$(parent).find(self.selectors.msg_block).text(text);
					}
				});
			return false;
			} else { 
				self._createIframe(this);
				return false;
			}
		}
		return true;
	}
	this._createIframe = function(form){  
		if (typeof $(form).attr("data-iframe") != "undefined") return false; // уже идет отправка;
		var iframeNumber = Math.floor((Math.random() * 1000) + 1);
		var target = "__ajaxUploadIFRAME"+iframeNumber;
		var iframe = $('<iframe id="'+target+'" name="'+target+'"></iframe>').attr('style','style="width:0px;height:0px;border:0px solid #fff;"').hide();
		$(iframe).attr('src', '');
		$(document.body).append(iframe); 
		var oldAction = $(form).attr("action");
		var newAction = $(form).attr("data-url");
		$(form).attr({"target" : target,
				"data_iframe" : iframeNumber,
				"action" : newAction});
		$(form).submit();       
		$(iframe).on('load',function(){
				var data = $(iframe).contents().find( "body" ).html();  
				if ((typeof data != "undefined") && (data != '')) { 
					if ( window.JSON && window.JSON.parse ) { 
						var newdata = JSON.parse(data);
					} else { 
						var newdata = !(/[^,:{}\[\]0-9.\-+Eaeflnr-u \n\r\t]/.test(
						data.replace(/"(\\.|[^"\\])*"/g, ''))) &&
						eval('(' + data + ')');
					}
					self._dataRender(newdata, $(form).parents(self.selectors.block));
					$(form).removeAttr("target").removeAttr("data-iframe").attr("action", oldAction);
					$(iframe).remove(); 
				}
		});	 
	} 
	//new part
	this.fileInsert = function (event) {
		var parent = $(this).parents(self.selectors.block);
		var files = event.target.files;
		for(var i = 0; i < files.length; i++) {    
			var file = files[i];
			var msg = self._validationImg(file);
			if (msg != '' ) {
				$(parent).find(self.selectors.msg_block).text(msg);
				return false;
			}
			var reader = new FileReader();
			reader.onload = function(event) {
				var img = new Image();
				img.onload = function() {
					$(parent).find(self.selectors.img_block).html("");
					$(parent).find(self.selectors.msg_block).html("");
					self._resize(img);
					$(img).appendTo($(parent).find(self.selectors.img_block));
				};
				img.src = event.target.result;
			};
			reader.onerror = function(event) {
				$(parent).find(self.selectors.msg_block).text("Файл "+file.name+"не может быть прочитан!  ");
			};
			reader.readAsDataURL(file);
		}
	}
	this._validationImg = function(file) {
		var mime_types = ["image/gif", "image/jpeg", "image/pjpeg", "image/png", "image/jpg"];
		var error = '';
		if (mime_types.indexOf(file.type) == -1) error += "Файл "+file.name+" недопустимого типа! ";
		if (file.size > 5*1024*1024) error += "Файл "+file.name+" слишком большой! ";
		return error;
	}
	this._resize = function(img) {
		var oldWidth = img.width;
		var oldHeight = img.height;
		var standartWidth = 100;
		var standartHeight = 100;
		if ((oldWidth/oldHeight) > (standartWidth / standartHeight)) {
			img.width = standartWidth;
			img.height = Math.ceil(standartWidth * oldHeight / oldWidth);
		} else {
			img.width = Math.ceil(standartHeight * oldWidth / oldHeight);
			img.height = standartHeight; 
		}
	}
	this._checkFiles = function(form) {
		var result = false;
		$(form).find('input[type=file]').each(function(i, elem){
			if($(elem).val() != "") {
				result = true;
				return false;
			}
		} );
		return result;
	}
	this._dataRender = function(data, parent) { 
		if (data.status == 'error' || data.status == "validation_error"){
			$(parent).find(self.selectors.msg_block).text(data.message);
		}
		else{
			//var result = data.data.replace(/&lt;/gi, "<");
			//result = result.replace(/&gt;/gi, ">");
			var html = data.data; //console.log(html);
			$($(html)).prependTo($(self.selectors.comments_block));
			$(parent).find(self.selectors.msg_block).text(""); 
			$(parent).find(self.selectors.img_block).html(""); 
			var inputs = $(parent).find(self.selectors.form).find('input, textarea');
			$(inputs).not('input[type=hidden]').not('input[type=submit]').val('');
			var text =$("div.coucomtitle").contents(":first").text();
			var number = parseInt(text);
			if (! isNaN(number) ) { 
				var newText = ++number + " "+ data.comm_caption;
				$("div.coucomtitle").contents(":first").replaceWith( newText );
			}
		}
	}
	this._formValidation = function(form) {
		var length = self.notEmpty.length;
		var emptyMsg = '';
		for (var i=0; i<length; i++ ) {
			if ( $(form).find(self.notEmpty[i][0]).val() == "" ) {
				emptyMsg += self.notEmpty[i][1]; 
			}
		}
		if (emptyMsg.length > 0) {
			$(form).parents(self.selectors.block).find(self.selectors.msg_block).text(emptyMsg);
			return false;
		}
		return true;
	}
}
$(function(){  
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
	CommentsRule.prototype.getCookie = getCookie; 
	var commentsBlock = new CommentsRule(null, [["textarea", "текст комментария не должен быть пуст!"]]);
	commentsBlock.init();
	});


