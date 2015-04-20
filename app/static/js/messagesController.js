/**
 * Controls the project page that overviews deliverables for students and professors
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('MessagesController', function ($scope, $http, $routeParams) {
	console.log('Started MessagesController');

	var self = this;
	self.loaded = false;
	self.message = "";

	self.project = {name: "Main Project"};

	self.messages = [
		{
			sender:"Randy Goodman", 
			username:"rxg4536",
			message:"I don't see you", 
			time:"2015-04-19T12:59:23+00:00"
		},
		{
			sender:"Chris Enoch", 
			username:"cxe3667",
			message:"I'm right here", 
			time:"2015-04-19T13:00:35+00:00"
		},
		{
			sender:"Ryan Bega",
			username:"rxb4678",
			message:"Well, I don't see either of you", 
			time:"2015-04-19T13:02:53+00:00"
		}];

	self.send = function() {
		self.messages.unshift({
			sender: $scope.app.user.fname + ' ' + $scope.app.user.lname,
			username: $scope.app.user.id,
			message: self.message, 
			time: "2015-04-19T13:02:53+00:00"
		});
		
		self.message = "";
	};
});
