/**
 * 
 */

var app = angular.module('flaskApp');

app.controller('HomeController', function($http){
	
	console.log("Created Home Controller");
	
	var self = this;
	self.loaded = false;
	self.mode = null;
	
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