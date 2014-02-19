
define([

	'angular',
	'angular.route',
	'angular.resource',
	'angular.ui.bootstrap',
	'./controllers/index',
	'./directives/index',
	'./services/index',
	'./filters/index',
	'config'

], function (angular) {
	'use strict';
    return angular.module('app', [
    	'ngRoute',
    	'ngResource',
    	'ui.bootstrap',
    	'app.controllers',
    	'app.directives',
    	'app.services',
    	'app.filters',
    	'app.constants'
    ]);
});
