/**
 * Index controller definition
 * @scope Controllers
 */
define(['../module'], function (controllers) {
  'use strict';
  controllers.controller('IndexController', ['$scope', function ($scope) {

    $scope.delay = 7000;
    $scope.tint = 'tint-white';

  }]);
});
