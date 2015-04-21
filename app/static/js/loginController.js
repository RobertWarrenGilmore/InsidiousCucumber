/**
 * Controls the project page that overviews deliverables for students and professors
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('LoginController', function ($scope, $http, $location) {
	console.log('Started LoginController');

	var self = this;
	
	self.checkUser = function() {
		$http.post('/auth/login', {username:self.username, password:self.password}).
			success(function(data, status, headers, config) {
				if (data.success) {
					$location.path('/home');
				} else {
					self.invalidPass = true;
				}
			}).
			error(function(data, status, headers, config) {
				self.invalidPass = true;
		});
	};
});
