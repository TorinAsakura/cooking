slider = new Array();
big = new Array();
big["width"] = 105;
big["height"] = 105;
big["height2"] = big["height"] + 28;
small = new Array();
small["width"] = 86;
small["height"] = 86;
small["height2"] = small["height"] + 28;
font = new Array();
font["big"] = 0;
font["small"] = 10;
timer = -1;

function equilibrate() {
	$('#slider2 ul li').each(function(i) {
		d = Math.abs(actual - i);
		var a = $(this);
		var img = a.children('a').children('img');
		var ttl = a.children('.imtitle');
		switch(d) {
			case 0:
				img.animate({width: big["width"], height: big["height"]});
				a.animate({width: big["width"] + 6 + 'px', height: big["height2"]}, function () { ttl.css({'font-size': font["big"]+'px'}); });
				showtext(a.attr('id').substr(5));
			break;
			case 1:
				ttl.css({'font-size': font["small"]+'px'});
				//if (a.css('display') == 'none') {
				if (slider[i] == 1) {
					slider[i] = 0;
					a.css({display: 'block', width: '0px', height: '0px'});
					img.css({width: '0px', height: '0px'});
					ttl.css({opacity: '0'});
				}
				img.animate({width: small["width"], height: small["height"]}, function () { ttl.fadeTo(500, 1); });
				a.animate({width: small["width"] + 6 + 'px', height: small["height2"]});
			break;
			default:
				if (slider[i] != 1) {
					slider[i] = 1;
					a.hide('fast');
				}
			break;
		}
	});
	directlink();
	rotate();
}
function actual_change(diff) {
	if (actual + diff > 0 && actual + diff < max) {
		actual = actual + diff;
		return true;
	}
	return false;
};
function directlink() {
	$('#directlink').attr('href', location.href.replace(location.search, '') + '?show=' + actual);
}
$(document).ready(function(){
	var requete = location.search.substring(1);
	var tab_paires = requete.split("&");
	var tab_elts = new Array();
	for (var i = 0; i < tab_paires.length; i++) {
		temp = tab_paires[i].split("=");
		tab_elts[temp[0]] = unescape(temp[1]);
	}

	$('#slider2 ul').css('overflow', 'hidden');
	max = $('#slider2 ul li').size();

	i = (tab_elts["show"]) ? parseInt(tab_elts["show"]) : 0;
	actual = (!isNaN(i) && i > 0 && i < max) ? i : 1;


	$('#slider2 ul li').each( function(i) {
		d = Math.abs(actual - i);
		var a = $(this);
		var img = a.children('a').children('img');
		var ttl = a.children('.imtitle');
		switch(d) {
			case 0:
				ttl.css({'font-size': font["big"]+'px'});
				img.css({width: big["width"]+'px', height: big["height"]+'px'});
				a.css({width: big["width"]+ 6 + 'px', height: big["height2"]+'px'});
				showtext(a.attr('id').substr(5));
			break;
			case 1:
				img.css({width: small["width"]+'px', height: small["height"]+'px'});
				a.css({width: small["width"] + 6 +'px', height: small["height2"]+'px'});
			break;
			default:
				a.css({display: 'block', width: '0px', height: '0px'});
			break;
		}
	});
	$('#butleft').click( function () {
		if (actual_change(-1))
			equilibrate();
		//timer_stop();
		return false;
	});
	$('#butright').click( function () {
		if (actual_change(+1))
			equilibrate();
		//timer_stop();
		return false;
	});
	

});
/*function timer_stop() {
	var a = $('#playpause').children('img').attr('src');
	var a = a.split("/");
	if (a[a.length - 1] == 'pause.png') {
		$('#playpause').children('img').attr('src', 'images/playred.png'); 
		window.clearInterval(timer);
	}
}*/
function next() {
	if (actual_change(+1))
		equilibrate();
}
function rotate() {
	//alert(max + ' ' + actual + ' ' + (max - actual));
/*
	if (actual < (max / 2)) {
		var a = $('#slider2 ul li').eq(max-1).remove();
		$('#slider2 ul').prepend(a);
		actual = actual + 1;
	}

		if (diff < 0) {
			var a = $('#slider2 ul li:last').remove();
			$('#slider2 ul').prepend(a);
		}
		else {
			var a = $('#slider2 ul li:first').remove();
			$('#slider2 ul').append(a);
		}
*/
}

function showtext(id) {
	$('#texts .text').each( function (i) {
		if ($(this).css('display') != 'none')
			//$(this).fadeOut('fast');
			$(this).fadeOut();
	});
	$('#texts #text'+id).fadeIn();
}







