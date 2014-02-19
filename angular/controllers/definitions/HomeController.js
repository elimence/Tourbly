
/**
 * Home controller definition
 * @scope Controllers
 */

define(['../module'], function (controllers) {
  'use strict';
  controllers.controller('HomeController', ['$scope', function ($scope) {

    var arrivalPicker = $('#arrival').pickadate().pickadate('picker');
    var departurPicker = $('#departure').pickadate().pickadate('picker');
    // attachSearchButtonListener();
    $('.carousel').carousel({
      interval: 25000
    });
    $('#select-beast').selectize({
      sortField: {
        field: 'text',
        direction: 'asc'
      },
      dropdownParent: 'body'
    });

  }]);
});
