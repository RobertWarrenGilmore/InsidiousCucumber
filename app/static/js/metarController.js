/**
 * 
 */

var app = angular.module('flaskApp');

app.controller('MetarController', function($http, metarService){
	console.log("Started MetarController");
	
	var self = this;
	self.loaded = false;
    
	var promise = null;
	
	self.abortRequest = function() {return(promise && promise.abort()); };
    
	function logData(){
		console.log(promise);
	}
	
	self.makeSearch = function(){
		self.search(self.query);
	}
	
	self.search = function(station){
		self.loaded = false;
		self.metar = {};
		console.log("Got Station data for: " + station)
		promise = metarService.getMetar(station); 
		promise.then(
				function(metarData) {
					console.log(metarData);
					self.metar = metarData.data;
					self.loaded = true;
				}, function( errorMessage ){
					self.loaded = true;
					console.warn("Request for Metar was rejected");
					console.warn("Error: ", errorMessage);
				});
		logData();
	};
	
	self.searchAll = function(){
		self.loaded = false;
		self.metar = {};
		stations = ['KROC', 'KBUF', 'KNYC', 'KPOU']
		promise = metarService.getAllMetar(stations);
		promise.then(
				function(metarData) {
					console.log(metarData);
					//$scope.metar = metarData.data;
					//$scope.loaded = true;
				}, function( errorMessage ){
					$scope.loaded = true;
					console.warn("Request for Metar was rejected");
					console.warn("Error: ", errorMessage);
				});
	}
	
});