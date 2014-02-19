define(['../module'], function(directives){

	directives.directive('slideMagic', ['$timeout', function($timeout) {

		var _scope;
		var slides;
		var delay = 7000;
		var slideIndex = 0;
		var curentSlide;

		var slide = function() {
			updateSlider();
    		$timeout(slide, delay, false);
    		advanceSlide();
		};

		var updateSlider = function() {
			console.log(curentSlide.index);
			_scope.tint = curentSlide.tint;
			$('#wrapper').css('background-image', 'url("' + curentSlide.src + '")'); // Next Image
			$('.navbar-brand img').attr('src', curentSlide.logo);
		};

		var advanceSlide = function() {
			slideIndex = curentSlide.index == (slides.length - 1) ? 0 : (curentSlide.index + 1);
			curentSlide = slides[slideIndex];
		}

	    return {
	    	restrict: 'ACE',

	    	link: function (scope, lElement, attrs) {

	    		_scope = scope;
	    		slides = scope.slides;
	    		curentSlide = slides[slideIndex];
	    		slide();

	    		lElement.bind('click', function(evt) {
	    			// use $digest instead of $apply to avoid
	    			// dirty checking from $rootscope
	    			scope.$apply(function() {
	    				// scope.tint = 'tint-black';
	    			});
	    		});

	    	}// end link function
	    }// end return
	}]);
});
