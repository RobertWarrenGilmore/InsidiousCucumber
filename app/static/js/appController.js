/**
 * The App Controller which acts as a global controller for the main HTML
 * template and all page elements.  It controls many aspects that need to
 * be on each page such as user information.
 */

/*global angular*/
'use strict';

var app = angular.module('minerva', ['ngRoute', 'ui.bootstrap', 'ui.calendar', 'lvl.directives.dragdrop']);

/*GLOBAL CONTROLLER*/
app.controller('AppController', function ($http) {
	console.log('Creating App Controller');

	var self = this;

	self.user = {};

	$http.get('/user').
			success(function(data, status, headers, config) {
				if (data.first != undefined) {
					self.user = {
						first: data.first,
						last: data.last,
						username: data.username,
						type: data.type,
						courses: data.courses,
					};
				}
			}).
			error(function(data, status, headers, config) {
				
		});
});
