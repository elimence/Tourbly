define(['../module'], function(filters){

	filters.filter('slideMagic', function() {
	    return {
	    	restrict: 'ACE',
	    	template: '<div class="content container">'+
				      '<div class="row">'+
				        '<div class="col-lg-12 lead-copy" style="border: 0px solid #000;">'+
				          '<h2 class="auxilliary preamble text {{tint}}">Managing your</h2>'+
				          '<h1 class="main text {{tint}}">Payroll</h1>'+
				          '<h3 class="auxilliary postamble text {{tint}}">Should be Easy As Pie.</h3>'+
				          '<a href="#" class="get-started">Get Started</a>'+
				        '</div>'+
				      '</div>'+
				    '</div>',

	    	link: function (scope, lElement, attrs) {

	    	}// end link function
	    }// end return
	});
});
