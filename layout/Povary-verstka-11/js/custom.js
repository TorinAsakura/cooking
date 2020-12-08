 jQuery(document).ready(function() {
	
	//top search
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
	
	//scrollable galleries
	$("#scrollable").scrollable({circular:true, prev:'#prev1', next:'#next1'});
	$("#scrollable2").scrollable({circular:true, prev:'#prev2', next:'#next2'});
	
	$("#slideshow .navi").tabs("#slideshow .item", {
    effect: 'fade',
    fadeOutSpeed: 1200,
	rotate: true
    }).slideshow({autoplay:true, interval:5000});
	
	
	// tabs	

	$("#main1 ul.tabs").tabs("#main1 div.panes > div");
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
		if ($('.search-text').val().length == 0) {
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
    }).blur();
    $('[placeholder]').parents('form').submit(function() {
        $(this).find('[placeholder]').each(function() {
            var input = $(this);
            if (input.val() == input.attr('placeholder')) {
                input.val('');
            }
        })
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
			$( "#amount1" ).text( ui.value);
			$('#range1 .ui-slider-handle').addClass('black-class');
			if ($("#amount1").text() == $("#range1").slider( "option", "max")){
				$("#amount1").text("Любой");
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
			$( "#amount2" ).text( ui.value);
			$('#range2 .ui-slider-handle').addClass('black-class');
			if ($("#amount2").text() == $("#range2").slider( "option", "max")){
				$("#amount2").text("Любое");
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
			$( "#amount3" ).text( ui.value );
			if ($("#amount3").text() == $("#range3").slider( "option", "max")){
				$("#amount3").text("No preference");
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
			$( "#amount4" ).text( ui.value );
			if ($("#amount4").text() == $("#range4").slider( "option", "max")){
				$("#amount4").text("No preference");
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
			$( "#amount5" ).text( ui.value );
			if ($("#amount5").text() == $("#range5").slider( "option", "max")){
				$("#amount5").text("No preference");
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
			$( "#amount6" ).text( ui.value );
			if ($("#amount6").text() == $("#range6").slider( "option", "max")){
				$("#amount6").text("No preference");
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
			$( "#amount7" ).val( ui.value );
		}
	});
	$("#range8").slider({
		min: 0,
		max: 200,
		values: [0,200],
		range: true,
		stop: function(event, ui) {
			jQuery("input#minamount").val(jQuery("#range8").slider("values",0));
			jQuery("input#maxamount").val(jQuery("#range8").slider("values",1));
		},
		slide: function(event, ui){
			jQuery("input#minamount").val(jQuery("#range8").slider("values",0));
			jQuery("input#maxamount").val(jQuery("#range8").slider("values",1));
		}
	});
	$( "#range9" ).slider({
		range: "min",
		value: 100,
		min: 1,
		max: 100,
		slide: function( event, ui ) {
			$( "#amount9" ).text( ui.value);
			$('#range9 .ui-slider-handle').addClass('black-class');
			if ($("#amount9").text() == $("#range9").slider( "option", "max")){
				$("#amount9").text("No preference");
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
				}
				return false
			});
			
			asd.find('span.plus').click(function() {
				var data = asd.find('input').val();
				asd.find('input').val(parseInt(data) + 1);
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
	
  
});





	



