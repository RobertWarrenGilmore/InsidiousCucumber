/**
 * Controls the flow for the homepage of courses and projects
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('HomeController', function ($scope, $http, $location) {

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

	self.init = function() {
		var usercourses = $scope.app.user.courses;
		
		if (usercourses != undefined) {
			for (var i = 0; i < usercourses.length; i++) {
				$http.get('/course/' + usercourses[i]).
					success(function(data, status, headers, config) {
						var temp = {};
						temp.course_id = data.course_id;
						temp.name = data.name;
						temp.description = data.description;
						temp.projects = [];
						self.courses.push(temp);
						for (var j = 0; j < data.projects.length; j++) {
							$http.get('/project/' + data.projects[i]).
								success(function(data, status, headers, config) {
									self.courses[i].projects.push(data);
								}).error(function(data, status, headers, config) {
									self.error = true;
								});
						}
					}).error(function(data, status, headers, config) {
						self.error = true;
					});
			}
		}
	};

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

	self.init();
});
