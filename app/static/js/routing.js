/**
 * 
 */

var app = angular.module('minerva');

/*PROVIDES URL ROUTING FOR THE APP*/
app.config(function ($routeProvider) {
	$routeProvider.when('/', {
		templateUrl: 'static/partials/home.html',
		controller: 'HomeController',
		controllerAs: 'homeCtrl'
	}).when('/metar', {
		templateUrl: 'static/partials/metar.html',
		controller: 'MetarController',
		controllerAs: 'metarCtrl'
	}).when('/metar/Results', {
		templateUrl: 'static/partials/metarResults.html',
	}).otherwise({ redirectTo: '/' });
});