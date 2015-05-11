/**
 * Controls the project page that overviews projects for students and professors
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('ProjectController', function ($http, $routeParams, $location) {
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

	self.init = function() {
		$http.get('/project/' + $routeParams.id).
			success(function(data, status, headers, config) {
				self.project = data;
			}).error(function(data, status, headers, config) {
				self.error = true;
			});
	};

	self.updateProject = function() {
		$http.put('/project/' + self.project.project_id, self.project).
			success(function(data, status, headers, config) {
				projectCtrl.edit = false;
			}).error(function(data, status, headers, config) {
				self.error = true;
			});
	}

	self.gotoDeliverables = function () {
		$location.search('id', self.project.project_id);
		$location.path('/deliverables');
	};

	self.gotoMessages = function () {
		$location.search('id', self.project.project_id);
		$location.path('/messages');
	};

	self.gotoTasks = function () {
		$location.search('id', self.project.project_id);
		$location.path('/tasks');
	};

	self.gotoMeetings = function () {
		$location.search('id', self.project.project_id);
		$location.path('/meetings');
	};

	self.gotoTeamManagement = function () {
		$location.search('id', self.project.project_id);
		$location.path('/teamManagement');
	};

	self.gotoTeamPreferenceSurvey = function () {
		$location.path('/teamPreferenceSurvey');
	};

	self.init();
});
