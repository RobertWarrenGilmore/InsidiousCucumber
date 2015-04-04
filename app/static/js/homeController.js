/**
 * 
 */

var app = angular.module('minerva');

app.controller('HomeController', function($http){
	
	console.log("Created Home Controller");
	
	var self = this;
	self.loaded = false;
	self.mode = null;
	

	self.courses = [{"name":"Eng of Enterprise SW Systems", "projects":[
		{"id":"1", "name":"Main Project", "notifications":["3 Unread Messages",
		"Deliverable 1 due 4/7/2015", "3 New Tasks Assigned"], "team":"Group 4"},
		{"id":"2", "name":"Research Project", "notifications":["Research Paper due 5/10/2015"], 
		"team":"Group 3"}]},
		{"name":"SW Process and Project Manage", "projects":[
		{"id":"3", "name":"PM Project", "notifications":[], "team":"Group 1"}]}
		];

	self.init = function(){
		console.log("Making HTTP Request");
		$http({
			method : 'GET',
			url : '/angularUpdate',
		}).success(function(data){
			console.log(data);
			self.mode = data.mode,
			self.searchUrl = data.classSearch
			self.loaded = true;
		});
	}

	self.gotoProject = function(id) {
		alert(id);
	}
	
	self.init();
});