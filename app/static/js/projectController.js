/**
 * Controls the project page that overviews projects for students and professors
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('ProjectController', function ($http, metarService, $routeParams, $location) {
	console.log('Started ProjectController');

	var self = this;
	self.loaded = false;

	self.projects = [{
		'id': '1',
		'name': 'Main Project',
		'description': 'Students will define and develop an information-based' +
			' enterprise application. Teams are given the freedom to select and specify the application or ' +
			'technology of their choosing so long as it fits within the project guidelines stated below and ' +
			'meets with the approval of the instructor.',
		'notifications': ['3 Unread Messages',
			'Deliverable 1 due 4/7/2015', '3 New Tasks Assigned'
		],
		'team': 'Group 4',
		'numteams': 8,
		'url': 'http://www.se.rit.edu/~swen-343/projects/EnterpriseApp/EnterpriseProjectStudentsChoice.html'
	}, {
		'id': '2',
		'name': 'Research Project',
		'description': 'Select a project that has “significant” ' +
			'information-related requirements. This does not necessarily mean a large (volume) of data or ' +
			'complicated application functionality, rather, it should have some reasonably complicated ' +
			'application functionality (more than just entering and displaying data in a GUI-over-Database ' +
			'web site) and the dependence on a relational database system being present.',
		'notifications': ['Research Paper due 5/10/2015'],
		'team': 'Group 3',
		'numteams': 5,
		'url': 'http://www.se.rit.edu/~swen-343/projects/EnterpriseApp/EnterpriseProjectStudentsChoice.html'
	}, {
		'id': '3',
		'name': 'PM Project',
		'description': 'Your team will create a Software Development Plan (SDP) based on the following problem statement.  ' +
			'The goal of the assignment from our courses perspective is to create a plan for executing the entire ' +
			'project, not a completed implementation.  Though you will not have time to develop the actual system, ' +
			'it may be good idea to familiarize yourself with the required technology in order to produce a more ' +
			'accurate plan.',
		'notifications': [],
		'team': 'Group 1',
		'numteams': 13,
		'url': 'http://www.se.rit.edu/~swen-256/projects/project.html'
	}];

	self.project = {};

	for (var i = 0; i < self.projects.length; i++) {
		if (self.projects[i].id === $routeParams.id) {
			self.project = self.projects[i];
		}
	}

	self.gotoDeliverables = function () {
		$location.search('id', self.project.id);
		$location.path('/deliverables');
	};

	self.gotoMessages = function () {
		$location.search('id', self.project.id);
		$location.path('/messages');
	};

	self.gotoTasks = function () {
		$location.search('id', self.project.id);
		$location.path('/tasks');
	};

	self.gotoTeamManagement = function () {
		$location.search('id', self.project.id);
		$location.path('/teamManagement');
	};

	self.gotoTeamPreferenceSurvey = function () {
		$location.path('/teamPreferenceSurvey');
	};

	var promise = null;

	self.abortRequest = function () {
		return (promise && promise.abort());
	};

	function logData() {
		console.log(promise);
	}

	self.makeSearch = function () {
		self.search(self.query);
	};

	self.search = function (station) {
		self.loaded = false;
		self.metar = {};
		console.log('Got Station data for: ' + station);
		promise = metarService.getMetar(station);
		promise.then(
			function (metarData) {
				console.log(metarData);
				self.metar = metarData.data;
				self.loaded = true;
			},
			function (errorMessage) {
				self.loaded = true;
				console.warn('Request for Metar was rejected');
				console.warn('Error: ', errorMessage);
			});
		logData();
	};
});
