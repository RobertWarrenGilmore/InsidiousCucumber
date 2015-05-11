/**
 * Controls the project page that overviews deliverables for students and professors
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('MeetingsController', function($http, $routeParams) {
	console.log('Started MeetingsController');

	var self = this;
	self.loaded = false;

	self.projects = [{
		'id': '1',
		'name': 'Main Project',
		'meetings': [{events: [{
			title:"Weekly Meeting 1",
			start:"2015-05-13T13:00:00+00:00",
			end:"2015-05-13T14:00:00+00:00"
		},
		{
			title:"Weekly Meeting 2",
			start:"2015-05-20T13:00:00+00:00",
			end:"2015-05-20T14:00:00+00:00"
		}]}]
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

	self.add = function() {
		var start = new Date(Date.parse(self.startdate + " " + self.starttime));
		var end = new Date(Date.parse(self.enddate + " " + self.endtime));
		self.project.meetings[0].events.push({
			title: self.description,
			start: start.toISOString(),
			end: end.toISOString()
		});
		console.log(self.project.meetings);
	}
});
