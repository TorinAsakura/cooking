 jQuery(document).ready(function() {

	// Top search
	$(".search-link").toggle(function() {
		$("#header").stop().animate({
			marginTop: "0px"
		}, 500);
		$(".s-text").focus();
	}, function() {
		$("#header").stop().animate({
			marginTop: "-50px"
		}, 500);
	});
	// fancybox for main img article and recipe
	$(".img-fancybox").fancybox({
			'type' : 'image'               
	});
	// Scrollable galleries
    if ($("#scrollable").find('img').length > 0 )  {
	   $("#scrollable").scrollable({circular:true, prev:'#prev1', next:'#next1'});
    }
    if ($("#scrollable2").find('img').length > 0 )  {
	   $("#scrollable2").scrollable({circular:true, prev:'#prev2', next:'#next2'});
    }

	$("#slideshow .navi").tabs("#slideshow .item", {
        effect: 'fade',
        fadeOutSpeed: 1200
        // rotate: true
    }).slideshow({autoplay:true, interval:5000});   


    //	$("#main1 ul.tabs").tabs("#main1 div.panes > div");

     $(".tabs").each(function (index) {
        //get index if tab selected by 'current' class
        var initialIndex = $(this).find('li:has(a.current)').index();
        //if no class="current" was set index is -1
        initialIndex = initialIndex < 0 ? 0 : initialIndex;
        //init tabs using found index
        $(this).tabs("#main1 div.panes > div", {initialIndex: initialIndex});
    });


	$("#main2 ul.tabs").tabs("#main2 div.panes > div");
	$("#main3 ul.tabs").tabs("#main3 div.panes > div");
	$("#main4 ul.tabs").tabs("#main4 div.panes4 > div");
	$("ul.tabs2").tabs("div.panes2 > div");
	$("#setting-tabs1").tabs("#setting-panes1 .gray-block");
	$("#setting-tabs2").tabs("#setting-panes2 > div");
	$("#setting-tabs3").tabs("#setting-panes3 > div");
	$("#setting-tabs4").tabs("#setting-panes4 > div");
	$("#setting-tabs4").tabs("#setting-panes4 > div");
	$(".views").tabs(".search-results > div");


	$('input:password').dPassword();


	/* pop-up windows */
	$(".review").fancybox({
		autoHeight : false,
		fitToView   : true
	});

	$('#send-message').fancybox({
		'closeBtn':false,
		'onComplete' : function(){
			$('.pop-title .close').click(function(){
			  $.fancybox.close()
			});
		}
	});

    $('#photo').fancybox({
//		'closeBtn':false,
//		'onComplete' : function(){
//			$('.pop-title .close').click(function(){
//			  $.fancybox.close()
//			});
//		}
	});

	$('.corobka').fancybox({
		'closeBtn':false,
		'onComplete' : function(){
			$('.pop-title .close').click(function(){
			  $.fancybox.close()
			});
		}
	});
	$('#fav-pop').fancybox();
	$('#reate-album').fancybox();
	$('#edit-album').fancybox();
	$('#edit-album2').fancybox();
	$('#edit-foto').fancybox();
	$('#my-albums').fancybox();


	$(".fancybox-thumb").fancybox({
		wrapCSS : 'photo-lightbox-class',
		prevEffect	: 'none',
		nextEffect	: 'none',
		padding:0,
		helpers	: {
			title	: {
				type: 'outside'
			},
			thumbs	: {
				width	: 80,
				height	: 80
			},
			buttons	: {}
		}

	});

	//header search
	$('.search-text').focus(function() {
        $(this).parents(".search").addClass('focus');
        $('.s-bg').fadeOut();
    });

	$(document).click(function(event) {
		if (($('.search-text').length > 0) && ($('.search-text').val().length == 0)){
			if($(event.target).parents().index($('.search')) == -1) {
				$(".search").removeClass('focus');
				$('.s-bg').fadeIn();
			}
		}
	});

	$('.read').click(function() {
        $(this).parents("li").find('.list-in').toggle();
		$(this).parents("li").find(".input-row input").focus();
    });

	//custom form elements
	$(".checkbox-block").fancyfields();
	$(".radio-row").fancyfields();
	$(".save-table").fancyfields();
	$(".form-row").fancyfields();
	$(".mail-table").fancyfields();
	$(".custom-div").fancyfields();

	//tabs onmouseover
	$("#slideshow2 .slide-tabs").tabs("#slideshow2 .item", {event:'mouseover'});
	$("#slideshow3 .slide-tabs").tabs("#slideshow3 .item", {event:'mouseover'});

	//placeholder
    /*
	$('[placeholder]').focus(function() {
        var input = $(this);
        if (input.val() == input.attr('placeholder')) {
            input.val('');
            input.removeClass('placeholder');
        }
    }).blur(function() {
        var input = $(this);
        if (input.val() == '' || input.val() == input.attr('placeholder')) {
            input.addClass('placeholder');
            input.val(input.attr('placeholder'));
        }
    }).blur();   */
	$('[placeholder]').parents('form').submit(function() {
		$(this).find('[placeholder]').each(function() {
			var input = $(this);
			if (input.val() == input.attr('placeholder')) {
				input.val('');
			}
		})
	});
    // placeholder without bugs
	$('[placeholder]').live('focus', function(){
		var input = $(this);
		if (input.val() == input.attr('placeholder')) {
			input.val('');
			if (input.hasClass('placeholder') )  input.removeClass('placeholder');
		}
	} );
	$('[placeholder]').live('blur', function(){
		var input = $(this);
		if (input.val() == '' || input.val() == input.attr('placeholder')) {
			if (! input.hasClass('placeholder') ) input.addClass('placeholder');
			input.val(input.attr('placeholder'));
		}
	});
	jQuery('.d-carousel .carousel').jcarousel({
		scroll: 1
	});

	//add book, add ingredient
	var NewContent = '<div class="book"><input type="text" class="input-text"/><a class="close"></a></div>'
	var NewContent2 = '<div class="change-block"><span class="move"></span><input type="text" class="input-text"/><a class="close"></a></div>'
	var NewContent3 = '<div class="ing-line"><input type="text" class="ing-text" placeholder="С ингридиентом"/><a class="remove-ing"></a></div>'

	$("#addbook").click(function(){
		$(this).before(NewContent);
		$(".close").click(function(){
		  $(this).parents('.book').hide();
		});
    });

	$("#adding").click(function(){
		$(this).before(NewContent2);
		$(".close").click(function(){
		  $(this).parents('.change-block').hide();
		});
	});

	$(".choose").click(function(){
	   $('.cats').slideToggle();
	});
	$(".big-search2 .close").click(function(){
	   $('.cats').slideUp();
	});

	//tooltip
	$(".views a").tooltip({ effect: 'slide'});

	//range sliders
	$( "#range1" ).slider({
		range: "min",
		value: 100,
		min: 1,
		max: 100,
		slide: function( event, ui ) {
			$( "#amount1" ).val( ui.value);
			$('#range1 .ui-slider-handle').addClass('black-class');
			if ($("#amount1").val() == $("#range1").slider( "option", "max")){
				$("#amount1").val("Любой");
				$('#range1 .ui-slider-handle').addClass('black-class')
			} else {
				$('#range1 .ui-slider-handle').removeClass('black-class');
			}
		}
	});

	$( "#range2" ).slider({
		range: "min",
		value: 100,
		min: 1,
		max: 100,
		slide: function( event, ui ) {
			$( "#amount2" ).val( ui.value);
			$('#range2 .ui-slider-handle').addClass('black-class');
			if ($("#amount2").val() == $("#range2").slider( "option", "max")){
				$("#amount2").val("Любое");
				$('#range2 .ui-slider-handle').addClass('black-class')
			} else {
				$('#range2 .ui-slider-handle').removeClass('black-class');

			}
		}
	});

	$( "#range3" ).slider({
		range: "min",
		value: 100,
		min: 1,
		max: 100,
		slide: function( event, ui ) {
			$( "#amount3" ).val( ui.value );
			if ($("#amount3").val() == $("#range3").slider( "option", "max")){
				$("#amount3").val("No preference");
				$('#range3 .ui-slider-handle').addClass('black-class')
			} else {
				$('#range3 .ui-slider-handle').removeClass('black-class');
			}

		}
	});

	$( "#range4" ).slider({
		range: "min",
		value: 100,
		min: 1,
		max: 100,
		slide: function( event, ui ) {
			$( "#amount4" ).val( ui.value );
			if ($("#amount4").val() == $("#range4").slider( "option", "max")){
				$("#amount4").val("No preference");
				$('#range4 .ui-slider-handle').addClass('black-class')
			} else {
				$('#range4 .ui-slider-handle').removeClass('black-class');
			}

		}
	});

	$( "#range5" ).slider({
		range: "min",
		value: 100,
		min: 1,
		max: 100,
		slide: function( event, ui ) {
			$( "#amount5" ).val( ui.value );
			if ($("#amount5").val() == $("#range5").slider( "option", "max")){
				$("#amount5").val("No preference");
				$('#range5 .ui-slider-handle').addClass('black-class')
			} else {
				$('#range5 .ui-slider-handle').removeClass('black-class');
			}

		}
	});
	$( "#range6" ).slider({
		range: "min",
		value: 100,
		min: 1,
		max: 100,
		slide: function( event, ui ) {
			$( "#amount6" ).val( ui.value );
			if ($("#amount6").val() == $("#range6").slider( "option", "max")){
				$("#amount6").val("No preference");
				$('#range6 .ui-slider-handle').addClass('black-class')
			} else {
				$('#range6 .ui-slider-handle').removeClass('black-class');
			}

		}
	});
	$( "#range7" ).slider({
		range: "min",
		value: 1,
		min: 1,
		max: 19,
		slide: function( event, ui ) {
			$( ".amount7" ).val( ui.value );
		}
	});
	$("#range8").slider({
		min: 0,
		max: 200,
		values: [0,200],
		range: true,
		stop: function(event, ui) {
			jQuery("input.minamount").val(jQuery("#range8").slider("values",0));
			jQuery("input.maxamount").val(jQuery("#range8").slider("values",1));
		},
		slide: function(event, ui){
			jQuery("input.minamount").val(jQuery("#range8").slider("values",0));
			jQuery("input.maxamount").val(jQuery("#range8").slider("values",1));
		}
	});
	$( "#range9" ).slider({
		range: "min",
		value: 100,
		min: 1,
		max: 100,
		slide: function( event, ui ) {
			$( "#amount9" ).val( ui.value );
			$('#range9 .ui-slider-handle').addClass('black-class');
			if ($("#amount9").val() == $("#range9").slider( "option", "max")){
				$("#amount9").val("No preference");
				$('#range9 .ui-slider-handle').addClass('black-class')
			} else {
				$('#range9 .ui-slider-handle').removeClass('black-class');

			}

		}
	});
	$('#range1 .ui-slider-handle').addClass('black-class');
	$('#range2 .ui-slider-handle').addClass('black-class');
	$('#range3 .ui-slider-handle').addClass('black-class');
	$('#range4 .ui-slider-handle').addClass('black-class');
	$('#range5 .ui-slider-handle').addClass('black-class');
	$('#range6 .ui-slider-handle').addClass('black-class');
	$('#range9 .ui-slider-handle').addClass('black-class');


	$(".about .opener").click(function(){
	   $(this).next('.slide').slideToggle();
	   $(this).toggleClass('active');
	});

	$(".edit-link").click(function(){
	   $(this).next('.hidden-div').slideToggle(200);
	   $(this).toggleClass('active');
	});
	$(".bal .toggle").click(function(){
	   $(this).next('.hidden-inf').slideToggle(200);
	   $(this).toggleClass('active');
	});

	//number of servings
	$(function() {
		$('.numb').each(function() {
			var asd = $(this);
			asd.find('span.minus').click(function() {
				var data = asd.find('input').val();
				if(data > 0) {
					asd.find('input').val(parseInt(data) - 1);
                    $("#porion_form").submit();
				}
				return false
			});

			asd.find('span.plus').click(function() {
				var data = asd.find('input').val();
				asd.find('input').val(parseInt(data) + 1);
                $("#porion_form").submit();
				return false
			});

		});

	});

	$(".expand-div").click(function(){
	   $(this).prev('.hidden').slideToggle();
	   $(this).toggleClass('closed');
	});

	//archive tabs
	$(".tabs-line").tabs(".months", {

		rotate: true,
		next:'.forward',
		prev:'.backward',
		select: function( event, ui ) {}
    }).slideshow({clickable:false});

    $("#porion_form").submit(function() {

        var url = $(this).attr('action');

        $.ajax({
               type: "POST",
               url: url,
               data: $(this).serialize(), // serializes the form's elements.
               success: function(data)
               {
                   if (data.error){
                       alert(data.error);
                   } // show response from the php script.
               }
             });

        return false; // avoid to execute the actual submit of the form.
    });


    $(".wish").click(function(event) {

        event.preventDefault();
        var url = $(this).attr('href');

        $.ajax({
               type: "POST",
               url: url,
               success: function(data)
               {
                   if (data.error){
                       alert(data.error);
                   } // show response from the php script.
               }
             });

        return false; // avoid to execute the actual submit of the form.
    });

    $("#animate").click(function(){

        $('.exp').animate({
          "height": "toggle"

        }, 500 );

        if($(this).text() == "свернуть"){
           $(this).text("развернуть");
        } else {
           $(this).text("свернуть");
        }

	});

	$("#message").live('submit', function(evnt){
        evnt.stopPropagation();
		evnt.preventDefault();

		form_data = $(this).serializeArray();
		form_url = $(this).attr('data-url');

        console.log($(this).attr('data-url'), $(this))

		$.post(form_url, form_data, function(data){
			if (data.status == 'error' ){
		        alert(data.message);
			}
			else{
                console.log(data);
                $('#question_list').append('<a href="/messages/notices/' + $.parseJSON(data).id + '/">' + $.parseJSON(data).title + '</a><br>')
			}
		});
	});

     var url = ''

    $('.close_filter').live('click', function(evnt){
        evnt.stopPropagation();
        evnt.preventDefault();
        var p = $(this).parent();
        var type = p.attr('type');
        var value = p.attr('data-value');


        if (!url){
            url = location.href
        }

        var href = url;
        var reg = new RegExp('&?'+type+'='+value,"g");
        href=href.replace(reg, "");
        href=href.replace(/\?&/, "?");

        url = href;

        $.ajax({
            type: "GET",
            url: href,
            success: function(data)
            {
                $('.center-block').html(data);
                $(".views").tabs(".search-results > div");
                var sort_url = $('#recipes_sort').attr('href');
                sort_url = sort_url.replace(/\?&?/, '');
                url = url.replace(/&?(sort=[^&]*|order=[^&]*)#?/g, '');

//                console.log(sort_url, url + '&' + sort_url);

                url = url + '&' + sort_url;
                $('#recipes_sort').attr('href', url);
            }
        });

    })

    $("div.form-row").click(function() {
        var elem = $(this).find('#tooltip');
        elem.fadeIn(1000).delay(3000).fadeOut(1000);
    });

    $('.fileinput').live('change', function(evt){

        var styles = {
            'position':'absolute',
            'z-index':2
        };
        $(this).css(styles)

        var input = $(this);

        var files = evt.target.files;
        var f = files[0];
        var reader = new FileReader();

        reader.onload = (function(theFile) {
            return function(e) {

                input.before('<img style="width:243px;height:243px;position:absolute;z-index:1;" src="' + e.target.result + '">');

            };

        })(f);
        reader.readAsDataURL(f);

    });

    $('#extra-step').find(":input").prop( "disabled", true );


    $('#add-extra-step').live('click', function(event){
        var extra = $('#extra-step');
        var number = extra.attr('data-value');

        extra.attr('data-value', +number + 1);
        $("#id_steps-TOTAL_FORMS").val(+number + 1);


        extra.find(":input").prop( "disabled", false );
        var step = extra.html();
        extra.find(":input").prop( "disabled", true );


        step = step.replace(/__prefix__/g, number);
        step = step.replace(/__step__/g, +number + 1);

        $(this).remove();

        $('.steps-block').append(step, $(this));

    });

    $('.errors').each(function(){
        var sibling = $(this).siblings();
        var width = sibling.width();
        $(this).css({'margin-left': (width + 3) + 'px'});
    })


    var change_group = function (input,text,val){

        var group_input = input.parents('.form-col').next('div').find('.new-gr');

        if (val == "Создать новую" ){
            group_input.show();
        } else {
            group_input.hide();
        }

    };


    var bind_change_group = function(){
         $("[name*='ingredient_group']").fancyfields("bind","onSelectChange", change_group);
    };

    bind_change_group()



     var add_ingredient_row = function(current_ingredient){
            var extra = $('#extra-row');
            var number = extra.attr('data-value');

            extra.attr('data-value', +number + 1);
            $("#id_second-TOTAL_FORMS").val(+number + 1);

            var row = extra.html();

            row = row.replace(/__prefix__/g, number);
            row = row.replace(/extra-row-id/g, 'current');

            current_ingredient.css({'display': 'none'});
//            current_ingredient.find(":input").prop( "disabled", false );
            current_ingredient.removeAttr('id');
            current_ingredient.attr('data-list-ing', number);
            console.log('data-list-ing ' + number);
            $(row).attr('data-ingridient-id', number);

            current_ingredient.after(row);
     };

     var reset_selects =function(){
            var ff = $("#current > .form-row");
            ff.find('.ffSelect').remove();
            ff.fancyfields();
            bind_change_group()
     };

            // $(document).ready(function() {
            //     var current_ingredient = $('#current');

            //     current_ingredient.find("[name*='value']").keydown(function (e) {
            //         // Allow: backspace, delete, tab, escape, enter and .
            //         if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 190]) !== -1 ||
            //              // Allow: Ctrl+A
            //             (e.keyCode == 65 && e.ctrlKey === true) ||
            //              // Allow: home, end, left, right
            //             (e.keyCode >= 35 && e.keyCode <= 39)) {
            //                  // let it happen, don't do anything
            //                  return;
            //         }
            //         // Ensure that it is a number and stop the keypress
            //         if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            //             e.preventDefault();
            //         }
            //     });
            // });

    // Add Recipe. Step 2. Preparing ingridient list
    // delete this only information      
	//name*=value validation
	$('#current').find("[name*='value']").live('keyup', function(){             
            var text = $(this).val();
            text = text.replace(/\,/g, ".");
            text = text.match(/\d*\.?\d*/);
            $(this).val(text);             
	} );
	$(".half-right").find("span.delete-ingridient").live('click', function(){
        var number =  $(this).attr('data-ingrt-number');
        console.log('span : ' + number);
		$(this).parents('li').remove();
        $('[data-list-ing="' + number + '"]').remove();
	} );
    $('#add-ingredient').live('click', function(event){

        var current_ingredient = $('#current');

        var selected_group = current_ingredient.find(
            "[name*='ingredient_group']").val();
        var selected_name = current_ingredient.find(
            "[name*='ingredient_info']").val();
        var selected_value = current_ingredient.find(
            "[name*='value']").val();
        var selected_ing_info = current_ingredient.find(
            "[name*='addit_info']").val();
        var selected_measure = current_ingredient.find(
            "[name*='measure'] option:selected").text();

        if (selected_value == "" || selected_value == 0 ){
            // todo: Укажите правильное значения для поля - количество
			alert("Заполните поле количество ингридиента!");
            return false;
        }         
        if (selected_name){

            if (selected_group == "Создать новую"){


                var group_select = current_ingredient.find(
                    "[name*='ingredient_group']");

                var group_input = group_select.parents(
                    '.form-col').next('div').find('input');
                selected_group = group_input.val();

                group_input.attr('name', group_select.attr('name'));

                group_select.prop('disabled', true);

                $("[name*='ingredient_group']").append(
                    '<option value="' + selected_group +
                    '">' + selected_group + '</option>');

            }

            add_ingredient_row(current_ingredient);

            reset_selects();

            if (!selected_group) selected_group = 'Без группы';

            var choosen_ingridients_panel = $(".half-right");
            var group = choosen_ingridients_panel.find("h5:contains('" + selected_group + "')");

            if (!group.length){

                choosen_ingridients_panel.append('<h5>' + selected_group + '</h5><ul class="sort"></ul>');

                group = choosen_ingridients_panel.find("h5:contains('" + selected_group + "')");
            }

            // ingridient description
            if ((selected_ing_info) && !(selected_ing_info == "Здесь вы можете подчеркнуть особенность ингрииента. К примеру: “Соус купленный только в Мексике”")){
                var selected_ing_info_with_small_tag = '<small> (' +  selected_ing_info + ')<small>';
            } else {
                var selected_ing_info_with_small_tag = "";
            }
            var ingrt_number = $('#extra-row').attr('data-value') - 1;
            console.log("data-value " + ingrt_number);
            group.next('ul').append($(
                '<li class="sort-item"><span class="f-right">' +
                selected_value +
                ' ' +
                selected_measure +
                '</span>' +
                selected_name +
                selected_ing_info_with_small_tag +
				'<span class="delete-ingridient" data-ingrt-number="' + ingrt_number + '">X</span>' +
                '</li>')
            );            
            $( "div.half-right" ).sortable({ items: "ul > li" });
            $("[name*='ingredient_group']").fancyfields("bind","onSelectChange", change_group);

        }
      // end of form "add ingridient"
    });

     if ($('div.half-right').hasClass('return')){
          var li_elements = $('div.half-right').find('li');
          var span_elements = li_elements.find('.group');

         var groups = [];

         span_elements.each(function(index){

            var text = $(this).text();
            var ul = '<ul class="sort">' +
                        $(this).parent()[0].outerHTML +
                    '</ul>' ;

            if (!~groups.indexOf(text) ){
                groups.push(text);

                $('div.half-right').append(

                    '<h5>' + text + '</h5>' + ul
                );
            } else {
                var group = $('div.half-right').find("h5:contains('" + text + "')");
                group.next('ul').append(ul);
            }

            span_elements.parent().remove();
         });


         add_ingredient_row($('#current'));
         reset_selects();
         $( "div.half-right" ).sortable({ items: "ul > li" });
     }


    // Add Recipe. Step 3. Close preparing step
    $('a.close').live('click', function(event){
        event.preventDefault();

        var extra = $('#extra-step');
        var number = extra.attr('data-value');

        extra.attr('data-value', +number - 1);
        $("#id_steps-TOTAL_FORMS").val(+number - 1);


        var block = $(this).parents('.step');
        var title = block.prev();

        block.remove();
        title.remove();


        $( "div.step-title:visible").each(function(index){
           $(this).text( (index + 1) + ' шаг');
        });

    });


    $(document).on('click', '#next_step', function (event){
       if($(this).hasClass('prevented')){
           event.preventDefault();

           var extra = $('#extra-row');
           var number = extra.attr('data-value');

           if (number - 1 != 0){
                $(this).removeClass('prevented');
                $(this).trigger('click');
           } else{
                $('#tooltip2').fadeIn(1000).delay(3000).fadeOut(1000);
           }

       }else{
           $(this).addClass('prevented');
           var forms_count_input = $("#id_second-TOTAL_FORMS");
           var forms_count = forms_count_input.val();
           forms_count_input.val(+forms_count - 1);

           $('#current, #extra-row').find(':input').prop('disabled', true);
       }
    });

});
