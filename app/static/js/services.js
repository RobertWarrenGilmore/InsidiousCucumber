/**
 * For Reference:
 * http://www.bennadel.com/blog/2616-aborting-ajax-requests-using-http-and-angularjs.htm
 */

var app = angular.module('flaskApp');

app.factory('metarService', function($http, $q){
	
	function getMetar(station){
		
		var deferredAbort = $q.defer();
		
		var request = $http({
			method : 'GET',
			url : '/metar/search',
			params: {station: station},
			timeout: deferredAbort.promise
		});
			
		//Promise to be returned
		var promise = request.then(
				function(response){
					return( response.data );
				},
				function( response ){
					return($q.reject("Something went wrong"));
				});
		
		promise.abort = function(){
			deferredAbort.resolve();
		}
		
		promise['finally'](
				function(){
					console.info("Cleaning up all references");
					
					promise.abort = angular.noop;
					
					deferredAbort = request = promise = null;
				});
			
		return(promise);
	}
	
	function getAllMetar(stations){
		
		var deferredAbort = $q.defer();
		var requests = [];
		console.log(stations);
		for(var i = 0; i < stations.length; i++ ){
			var station = stations[i];
			console.log(station);
			requests.push($http({
				method : 'GET',
				url : '/metar/search',
				params: {station: station},
				timeout: deferredAbort.promise
			}));
		}
		
		//Promise to be returned
		var promise = $q.all(requests).then(
				function(response){
					return( response );
				},
				function( response ){
					console.log(response);
					return($q.reject("Something went wrong"));
				});
		
		promise.abort = function(){
			deferredAbort.resolve();
		}
		
		promise['finally'](
				function(){
					console.info("Cleaning up all references");
					
					promise.abort = angular.noop;
					
					deferredAbort = requests = promise = null;
				});
			
		return(promise);
	}
	
	return({
		getMetar: getMetar,
		getAllMetar: getAllMetar
	});
});