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

	self.project = {
		name: 'Main Project'
	};

	self.classmates = [{
		name: 'Robert Gilmore'
	}, {
		name: 'Randy Goodman'
	}, {
		name: 'Ryan Bega'
	}, {
		name: 'Christopher Enoch'
	}, {
		name: 'Petunia Jones'
	}, {
		name: 'Ben Schiller'
	}, {
		name: 'Phil Cook'
	}, {
		name: 'Ringo Starr'
	}, {
		name: 'Master Chief'
	}, {
		name: 'Sanic'
	}, {
		name: 'Phillip J. Fry'
	}, {
		name: 'Georgia Lass'
	}, {
		name: 'Victor Frankenstein'
	}, {
		name: 'Nathan Explosion'
	}, {
		name: 'Arturo Sandoval'
	}, {
		name: 'Marie Curie'
	}, {
		name: 'Mel Brooks'
	}, {
		name: 'Barbara Streisand'
	}, {
		name: 'Marissa Tomei'
	}, {
		name: 'Kristen Schaal'
	}];
});
