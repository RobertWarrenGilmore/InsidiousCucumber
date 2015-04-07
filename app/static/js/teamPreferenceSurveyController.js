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
		name: 'Robert Gilmore',
		preference: 'no_preference'
	}, {
		name: 'Randy Goodman',
		preference: 'no_preference'
	}, {
		name: 'Ryan Bega',
		preference: 'no_preference'
	}, {
		name: 'Christopher Enoch',
		preference: 'no_preference'
	}, {
		name: 'Petunia Jones',
		preference: 'no_preference'
	}, {
		name: 'Ben Schiller',
		preference: 'no_preference'
	}, {
		name: 'Phil Cook',
		preference: 'no_preference'
	}, {
		name: 'Ringo Starr',
		preference: 'no_preference'
	}, {
		name: 'Master Chief',
		preference: 'no_preference'
	}, {
		name: 'Sanic',
		preference: 'no_preference'
	}, {
		name: 'Phillip J. Fry',
		preference: 'no_preference'
	}, {
		name: 'Georgia Lass',
		preference: 'no_preference'
	}, {
		name: 'Victor Frankenstein',
		preference: 'no_preference'
	}, {
		name: 'Nathan Explosion',
		preference: 'no_preference'
	}, {
		name: 'Arturo Sandoval',
		preference: 'no_preference'
	}, {
		name: 'Marie Curie',
		preference: 'no_preference'
	}, {
		name: 'Mel Brooks',
		preference: 'no_preference'
	}, {
		name: 'Barbara Streisand',
		preference: 'no_preference'
	}, {
		name: 'Marissa Tomei',
		preference: 'no_preference'
	}, {
		name: 'Kristen Schaal',
		preference: 'no_preference'
	}];
});
