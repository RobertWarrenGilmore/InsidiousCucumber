/**
 * Controls the project page that overviews deliverables for students and professors
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('LoginController', function ($scope, $http, $location) {
	console.log('Started LoginController');

	var self = this;
	
	$scope.app.user = {};

	self.users = [{
		'id': 'wes7817',
		'pass': 'test',
		'fname': 'Wayne',
		'lname': 'Starr',
		'professor': true
	}, {
		'id': 'cte6149',
		'pass': 'test',
		'fname': 'Chris',
		'lname': 'Enoch',
		'professor': false
	}];
	
	self.checkUser = function() {
		for (var i = 0; i < self.users.length; i++) {
			if (self.users[i].id === self.username && self.users[i].pass === self.password) {
				$scope.app.user = self.users[i];
				$location.path('/home');
			}
		}
		self.invalidPass = true;
	};
});
