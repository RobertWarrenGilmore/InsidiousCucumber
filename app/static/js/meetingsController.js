/**
 * Controls the project page that overviews deliverables for students and professors
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('MeetingsController', function ($http, $routeParams) {
	console.log('Started MeetingsController');

	var self = this;
	self.loaded = false;

	self.projects = [{
		'id': '1',
		'name': 'Main Project',
		'meetings': []
	}, {
		'id': '2',
		'name': 'Research Project',
		'meetings': []
	}, {
		'id': '3',
		'name': 'PM Project',
		'meetings': []
	}];

	self.project = {};

	for (var i = 0; i < self.projects.length; i++) {
		if (self.projects[i].id === $routeParams.id) {
			self.project = self.projects[i];
		}
	}
});
