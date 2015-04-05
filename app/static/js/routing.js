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
	}).when('/project', {
		templateUrl: 'static/partials/project.html',
		controller: 'ProjectController',
		controllerAs: 'projectCtrl'
	}).otherwise({ redirectTo: '/' });
});