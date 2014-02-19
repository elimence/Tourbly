/**
 * Defines the main routes in the application.
 * The routes you see here will be anchors '#/' unless specifically configured otherwise.
 */

define(['angular', 'app'], function (angular, app) {
  'use strict';

  app.config([
    '$routeProvider',
    '$locationProvider',
    function ($routeProvider, $locationProvider) {

    $locationProvider.html5Mode(true).hashPrefix('!');

      $routeProvider
        .when('/', {
          templateUrl: 'partials/home.html',
          controller: 'HomeController'
        })
        .when('/view2', {
          templateUrl: 'partials/partial2.html',
          controller: 'IndexController'
        })
        .when('/view3', {
          templateUrl: 'partials/partial3.html',
          controller: 'IndexController'
        })
        .otherwise({
          redirectTo: '/'
        });

    }]);
});
