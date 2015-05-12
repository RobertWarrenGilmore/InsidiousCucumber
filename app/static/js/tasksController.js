/**
 * Controls the project page that overviews deliverables for students and professors
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

app.controller('TasksController', function ($scope, $http, $routeParams) {
	console.log('Started TasksController');

	var self = this;
	self.loaded = false;

	self.team = {
		team_id: 12,
		name: "Group 1",
		members: [
			{name:"Randy Goodman", uid:"rxg4536"}, 
			{name:"Chris Enoch", uid:"cxe3667"}, 
			{name:"Ryan Bega", uid:"rxb4678"}
		],
		tasks: [
			{
				assigned:"Randy Goodman",
				uid:"rxg4536",
				description:"Implement Database",
				due:"2015-04-20T13:00:00+00:00"
			}, 
			{
				assigned:"Chris Enoch",
				uid:"cxe3667",
				description:"Implement API",
				due:"2015-04-20T13:00:00+00:00"
			}, 
			{
				assigned:"Ryan Bega",
				uid:"rxb4678",
				description:"Work on Documentation",
				due:"2015-04-20T13:00:00+00:00"
			}]
		};

	for (var i = 0; i < self.team.members.length; i++) {
		self.team.members[i].selected = "alert-warning";
	}

	self.add = function() {
		if (self.selected != undefined) {
			var d = new Date(Date.parse(self.duedate + " " + self.duetime));
			self.team.tasks.push({
				assigned: self.selected.name,
				uid: self.selected.uid,
				description: self.description, 
				due: d.toISOString()
			});
			console.log(self.team.tasks);
		} else {
			self.selectuser = true;
		}
	}

	self.remove = function(index) {
		self.team.tasks.splice(index, 1);
	}

	self.selectMember = function(member) {
		self.selected = member;
		for (var i = 0; i < self.team.members.length; i++) {
			self.team.members[i].selected = "alert-warning";
		}
		member.selected = "alert-info";
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
