/**
 * Created by TorinAsakura on 02.06.14.
 */
jQuery(function($) {
    var $form = $('#comment form');
    var file_input = $form.find('input[type=file]');
    var upload_in_progress = true;

    file_input.ace_file_input({
        style : 'well',
        btn_choose : 'Выберите файл или перетащите его сюда',
        btn_change: null,
        droppable: true,
        thumbnail: 'large',

        maxSize: 5120000,//bytes
        allowExt: ["jpeg", "jpg", "png", "gif"],
        allowMime: ["image/jpg", "image/jpeg", "image/png", "image/gif"],

        before_remove: function() {
            if(upload_in_progress)
                return false;//пока файло грузиться любые действия запрещены
            return true;
        },

        preview_error: function(filename , code) {
            //code = 1 ошибка при загрузке
            //code = 2 ошибка при загрузке картинки - это точно картинка? оО
            //code = 3 ошибка при рендере превью, мало ли что там
        }
    })

    file_input.on('file.error.ace', function(ev, info) {
        if(info.error_count['ext'] || info.error_count['mime']) alert('Неверный формат файла! Убедитесь, что это изображение!');
        if(info.error_count['size']) alert('Неверный формат файла! Максимальный размер 5120KB');

        //бекендщикам тут нефиг делать ^^
        //ev.preventDefault();
        //file_input.ace_file_input('reset_input');
    });

    var ie_timeout = null;//если браузер хрень - идём в лобовую через iframe

    $form.on('submit', function(e) {
        e.preventDefault();

        var files = file_input.data('ace_input_files');
        if( !files || files.length == 0 ) return false;//нет выбранных файлов? идём в задницу

        var deferred ;
        if( "FormData" in window ) {
            formData_object = new FormData();//создаём пустой FormData object

            $.each($form.serializeArray(), function(i, item) {
                formData_object.append(item.name, item.value);
            });
            $form.find('input[type=file]').each(function(){
                var field_name = $(this).attr('name');

                var files = $(this).data('ace_input_files');
                if(files && files.length > 0) {
                    for(var f = 0; f < files.length; f++) {
                        formData_object.append(field_name, files[f]);
                    }
                }
            });


            upload_in_progress = true;
            file_input.ace_file_input('loading', true);

            deferred = $.ajax({
                url: $form.attr('action'),
                type: $form.attr('method'),
                processData: false,//руки фу
                contentType: false,//руки фу
                dataType: 'json',
                data: formData_object
                /**
                 ,
                 xhr: function() {
								var req = $.ajaxSettings.xhr();
								if (req && req.upload) {
									req.upload.addEventListener('progress', function(e) {
										if(e.lengthComputable) {
											var done = e.loaded || e.position, total = e.total || e.totalSize;
											var percent = parseInt((done/total)*100) + '%';
											//готовность загрузки в процентах
										}
									}, false);
								}
								return req;
							},
                 beforeSend : function() {
							},
                 success : function() {
							}*/
            })

        }
        else {
            deferred = new $.Deferred

            var temporary_iframe_id = 'temporary-iframe-'+(new Date()).getTime()+'-'+(parseInt(Math.random()*1000));
            var temp_iframe =
                $('<iframe id="'+temporary_iframe_id+'" name="'+temporary_iframe_id+'" \
								frameborder="0" width="0" height="0" src="about:blank"\
								style="position:absolute; z-index:-1; visibility: hidden;"></iframe>')
                    .insertAfter($form)

            $form.append('<input type="hidden" name="temporary-iframe-id" value="'+temporary_iframe_id+'" />');

            temp_iframe.data('deferrer' , deferred);

            $form.attr({
                method: 'POST',
                enctype: 'multipart/form-data',
                target: temporary_iframe_id //руки фу
            });

            upload_in_progress = true;
            file_input.ace_file_input('loading', true);//рендерим оверлей с иконочкой
            $form.get(0).submit();


            //если в течение 30 секунд не получаем ответ - выводим еррор
            ie_timeout = setTimeout(function(){
                ie_timeout = null;
                temp_iframe.attr('src', 'about:blank').remove();
                deferred.reject({'status':'fail', 'message':'Время ожидания истекло!'});
            } , 30000);
        }


        ////////////////////////////
        deferred
            .done(function(result) {//success
                var message = '';
                for(var i = 0; i < result.length; i++) {
                    if(result[i].status == 'OK') {
                        message += "Файл успешно загружен. Превью: " + result[i].url
                    }
                    else {
                        message += "Файл не сохранён. " + result.message;
                    }
                    message += "\n";
                }
                alert(message);
            })
            .fail(function(result) {//ошибка
                alert("Что-то тут не так…");
            })
            .always(function() {//призывается при обоих случаях
                if(ie_timeout) clearTimeout(ie_timeout)
                ie_timeout = null;
                upload_in_progress = false;
                file_input.ace_file_input('loading', false);
            });

        deferred.promise();
    });

    $form.on('reset', function() {
        $(this).find('input[type=file]').ace_file_input('reset_input_ui');
    });

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
});