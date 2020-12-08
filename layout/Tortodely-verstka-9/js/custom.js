 jQuery(document).ready(function() {
	
	$(".search-link").toggle(function() {
		$("#header").stop().animate({
			marginTop: "0px"
		}, 500);
		$(".s-text").focus();
	}, function() {
		$("#header").stop().animate({
			marginTop: "-72px"
		}, 500);
	});
	
	$("#scrollable").scrollable({circular:true, prev:'#prev1', next:'#next1'});
	$("#scrollable2").scrollable({circular:true, prev:'#prev2', next:'#next2'});
	
	//$("ul.tabs").tabs("div.panes > div");
	
	var autoHeight = $('.search-results').height() + 27;
	$('.search-text').focus(function() {  
        $(this).parents(".search").addClass('focus');
    });  

	$(document).click(function(event) { 
		if($(event.target).parents().index($('.search')) == -1) {
			$(".search").removeClass('focus');
			$(".search-bottom").fadeOut();
		}        
	});
	
	
	function showDiv() {
		if ($(window).scrollTop() > 375 && $('.block-tabs').data('positioned') == 'false') {
			$(".block-tabs").hide().css({"position": "fixed", "top": "-26px"}).fadeIn().data('positioned', 'true');
			$('.block-tabs-center').hide();
			$('.tab1').removeClass('current');	
			$('.tab2').removeClass('current');	
			$(".block-tabs").addClass('fix');
		} else if ($(window).scrollTop() <= 375 && $('.block-tabs').data('positioned') == 'true') {
			$(".block-tabs").fadeOut(function() {
				$(this).css({"position": "relative", "top": "0px"}).show();
				$(".block-tabs").removeClass('fix');
			}).data('positioned', 'false');
		}
		
		if ($(window).scrollTop() > 1050 && $('.hidden-ingr').data('positioned') == 'false') {
			$(".hidden-ingr").hide().css({"position": "fixed", "top": "0px"}).fadeIn().data('positioned', 'true');
			
			$(".hidden-ingr").addClass('fix');
		} else if ($(window).scrollTop() <= 1050 && $('.hidden-ingr').data('positioned') == 'true') {
			$(".hidden-ingr").fadeOut(function() {
				$(this).css({"position": "relative", "top": "0px"}).show();
				$(".hidden-ingr").removeClass('fix');
			}).data('positioned', 'false');
		}
	}
	$(window).scroll(showDiv);
	$('.block-tabs').data('positioned', 'false');
	$('.hidden-ingr').data('positioned', 'false');
	
	
	$('.hidden-ingr h3').click(function() {
		$(this).toggleClass('act');		
		$('.hidden-ingr .ingridient').slideToggle();		
	});
	
	$('a.close-arrow').click(function() {
		$('.hidden-ingr .ingridient').slideToggle();		
	});
	
	/*$('.fancybox-thumbs li').click(function() {
		$('.fancybox-thumbs li').not(this).removeClass('active');		
		$(this).addClass('active');		
	});*/
	
	
	$('.ingredients ul li .close').click(function() {
		$(this).parent('li').hide();		
	});
	
	/* */
	$('.go-top').click(function () {
		$('body,html').animate({
			scrollTop: 0
		}, 800);
		return false;
	});
		
	$(".scroll").click(function(event){		
		event.preventDefault();
		$('html,body').animate({scrollTop:($(this.hash).offset().top) - 50}, 500);
	});	
	
	/* */
	
	$(".tab1").toggle(
        function () {
			$(this).addClass('current');		
		$('.tab2').removeClass('current');		
		$('.pane2').hide();		
		$('.pane1').show();		
		$('.block-tabs-center').slideDown();            
        }, 
        function () {
            $(this).removeClass('current');		
		$('.tab2').removeClass('current');		
		$('.pane2').show();		
		$('.pane1').show();		
		$('.pane2').hide();
		$('.block-tabs-center').slideUp(); 
        });
		
		
	$(".tab2").toggle(
        function () {
			$(this).addClass('current');		
		$('.tab1').removeClass('current');		
		$('.pane1').hide();		
		$('.pane2').show();	
		$('.block-tabs-center').slideDown();            
        }, 
        function () {
            $(this).removeClass('current');		
		$('.tab1').removeClass('current');		
		$('.pane2').show();		
		$('.pane1').show();		
		$('.pane1').hide();
		$('.block-tabs-center').slideUp();
        });	
	
	
	
	
	
	
	
	$(".fancybox-thumb").fancybox({
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
	
});


$(document).ready(function() {
	$('.tov-img').each(function() {
		$(".sm-imgs img").click(function() {
			// see if same thumb is being clicked
			if ($(this).hasClass("active")) { return; }
		 
			// calclulate large image's URL based on the thumbnail URL (flickr specific)
			var url = $(this).attr("src").replace("_t", "");
		 
			// get handle to element that wraps the image and make it semi-transparent
			var wrap = $(this).parents('.tov-img').find(".image_wrap").fadeTo("medium", 1);
		 
			// the large image from www.flickr.com
			var img = new Image();
		 

			// call this function after it's loaded
			img.onload = function() {
		 
				// make wrapper fully visible
				wrap.fadeTo("fast", 1);
		 
				// change the image
				wrap.find("img").attr("src", url);
		 
			};
		 
			// begin loading the image from www.flickr.com
			img.src = url;
		 
			// activate item
			$(this).parent().parent('.sm-imgs').find("img").removeClass("active");
			$(this).addClass("active");
		 
		// when page loads simulate a "click" on the first image
		}).filter(":first").click();
	});
	
	$('.addfoto-block-input').click(function() {
		$(this).addClass('act');				
	});
	
});	

$(document).ready(function(e) {
	try {
	$(".styled").msDropDown();
	} catch(e) {
	alert(e.message);
	}
});



	



