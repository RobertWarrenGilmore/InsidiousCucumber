/**
 * Controls the project page that overviews deliverables for students and professors
 */

var app = angular.module('minerva');

app.controller('DeliverablesController', function($http, $routeParams){
	console.log("Started DeliverablesController");
	
	var self = this;
	self.loaded = false;

	self.projects = [
		{"id":"1", "name":"Main Project", "deliverables":[]},
		{"id":"2", "name":"Research Project", "deliverables":[]},
		{"id":"3", "name":"PM Project", "deliverables":[]}];

	self.project = {};

	for (var i = 0; i < self.projects.length; i++) {
		if (self.projects[i].id == $routeParams.id) {
			self.project = self.projects[i];
		}
	}
});