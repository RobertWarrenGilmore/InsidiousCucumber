/**
 * Controls the team preference survey page
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('TeamPreferenceSurveyController', function ($http, metarService, $routeParams, $location) {
	console.log('Started TeamPreferenceSurveyController');

	var self = this;
	self.loaded = false;

	self.classmates = [{
		name: 'Robert Gilmore'
	}, {
		name: 'Randy Goodman'
	}, {
		name: 'Ryan Bega'
	}, {
		name: 'Christopher Enoch'
	}];
});
