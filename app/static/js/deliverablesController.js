/**
 * Controls the project page that overviews deliverables for students and professors
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('DeliverablesController', function ($http, $routeParams) {
	console.log('Started DeliverablesController');

	var self = this;
	self.loaded = false;

	self.projects = [{
		'id': 1,
		'name': 'Main Project',
		'deliverables': [{description:"Release 1", due:"2015-05-10T13:00:00+00:00"}]
	}, {
		'id': 2,
		'name': 'Research Project',
		'deliverables': [{description:"Release 1", due:"2015-04-20T13:00:00+00:00"}]
	}, {
		'id': 3,
		'name': 'PM Project',
		'deliverables': [{description:"Release 1", due:"2015-04-20T13:00:00+00:00"}]
	}];

	self.project = {};

	for (var i = 0; i < self.projects.length; i++) {
		if (self.projects[i].id == $routeParams.id) {
			self.project = self.projects[i];
		}
	}

	self.add = function() {
		var d = new Date(Date.parse(self.duedate + " " + self.duetime));
		self.project.deliverables.push({description: self.description, due: d.toISOString()});
	}

	self.remove = function(index) {
		self.project.deliverables.splice(index, 1);
	}

	self.compareDate = function(date, mode) {
		var d = new Date(Date.parse(date));
		var now = new Date();
		if (mode == 0 && d.getTime() < now.getTime()) {
			return true;
		} else if (mode == 1 && d.getTime() >= now.getTime() && (d.getTime() - 259200000) <= now.getTime()) {
			return true;
		} else if (mode == 2 && (d.getTime() - 259200000) > now.getTime()) {
			return true;
		} else {
			return false;
		}
	}

	self.parse = function(date) {
		var d = new Date(Date.parse(date));
		var out = "";
		out = out + self.zeropad(d.getHours()) + ":" + self.zeropad(d.getMinutes()) + ":" + 
			self.zeropad(d.getSeconds()) + " on " + self.zeropad((d.getMonth()+1)) + "/" + 
			self.zeropad(d.getDate()) + "/" + d.getFullYear();
		return out;
	}

	self.zeropad = function(num) {
		if (num < 10) {
			return '0' + num;
		} else {
			return '' + num;
		}
	}
});
