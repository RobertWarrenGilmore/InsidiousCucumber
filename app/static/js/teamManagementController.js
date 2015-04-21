/**
 * Controls the project page that overviews deliverables for students and professors
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('TeamManagementController', function ($scope, $http, $routeParams) {
	console.log('Started TeamManagementController');

	var self = this;
	self.loaded = false;

	self.project = {name: "Main Project"};

	self.teams = [
		{
			team_id: 12,
			name: "Team 1",
			members: ["Randy Goodman", "Chris Enoch", "Ryan Bega"]
		},
		{
			team_id: 10,
			name: "Team 2",
			members: ["Wayne Starr", "Robert Gilmore", "Betty White"]
		},
		{
			team_id: 4,
			name: "Team 3",
			members: ["Master Chief", "Princess Peach", "Donkey Kong"]
		}];

	self.add = function() {
		self.teams.push({
			team_id: 0,
			name: "Team " + (self.teams.length + 1),
			members: []
		});
	};

	self.dropped = function(dragEl, dropEl) {
		var drop = $( "#" + dropEl );
		var drag = $( "#" + dragEl );

		var name = drag.attr('data-name');
		var drag_team = drag.attr('data-team');

		var drop_team = drop.attr('data-team');

		for (var i = 0; i < self.teams[drag_team].members.length; i++) {
			if (self.teams[drag_team].members[i] == name) {
				self.teams[drag_team].members.splice(i, 1);
			}
		}
		
		self.teams[drop_team].members.push(name);
	
		$scope.$digest();
	};
});
