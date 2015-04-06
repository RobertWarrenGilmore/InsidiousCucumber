/**
 * Controls the flow for the homepage of courses and projects
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('HomeController', function ($http, $location) {

	console.log('Created Home Controller');

	var self = this;

	self.courses = [{
		'name': 'Eng of Enterprise SW Systems',
		'projects': [{
			'id': '1',
			'name': 'Main Project',
			'description': '',
			'notifications': ['3 Unread Messages',
				'Deliverable 1 due 4/7/2015', '3 New Tasks Assigned'
			],
			'team': 'Group 4',
			'numteams': 8
		}, {
			'id': '2',
			'name': 'Research Project',
			'description': '',
			'notifications': ['Research Paper due 5/10/2015'],
			'team': 'Group 3',
			'numteams': 5
		}]
	}, {
		'name': 'SW Process and Project Manage',
		'projects': [{
			'id': '3',
			'name': 'PM Project',
			'description': '',
			'notifications': [],
			'team': 'Group 1',
			'numteams': 13
		}]
	}];

	self.gotoProject = function (id) {
		$location.search('id', id);
		$location.path('/project');
	};

	self.addProject = function (course) {
		course.addProject = false;
		course.projects.push({
			'name': course.addProjectName,
			'description': course.addProjectDesc,
			'team': 'No Team Assigned',
			'numteams': 0,
			'notifications': []
		});
		course.addProjectName = '';
		course.addProjectDesc = '';
	};

	self.removeProject = function (course, project) {
		for (var i = 0; i < course.projects.length; i++) {
			if (course.projects[i] === project) {
				course.projects.splice(i, 1);
				break;
			}
		}
	};
});
