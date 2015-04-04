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
		{"name":"Main Project", "notifications":["3 Unread Messages",
		"Deliverable 1 due 4/7/2015"], "team":"Group 4"},
		{"name":"Research Project", "notifications":["1 Unread Message",
		"Research Paper due 5/10/2015"], "team":"Group 3"}]},
		{"name":"SW Process and Project Manage", "projects":[
		{"name":"PM Project", "notifications":["SDP Revision 1 due 4/5/2015",
		"3 New Tasks Assigned"], "team":"Group 1"}]}
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
	
	self.init();
});