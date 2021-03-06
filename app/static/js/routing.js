/**
 *
 */

/*global angular*/
'use strict';

var app = angular.module('minerva');

/*PROVIDES URL ROUTING FOR THE APP*/
app.config(function ($routeProvider) {
	$routeProvider.when('/', {
		templateUrl: 'static/partials/login.html',
		controller: 'LoginController',
		controllerAs: 'loginCtrl'
	}).when('/home', {
		templateUrl: 'static/partials/home.html',
		controller: 'HomeController',
		controllerAs: 'homeCtrl'
	}).when('/project', {
		templateUrl: 'static/partials/project.html',
		controller: 'ProjectController',
		controllerAs: 'projectCtrl'
	}).when('/deliverables', {
		templateUrl: 'static/partials/deliverables.html',
		controller: 'DeliverablesController',
		controllerAs: 'deliverablesCtrl'
	}).when('/messages', {
		templateUrl: 'static/partials/messages.html',
		controller: 'MessagesController',
		controllerAs: 'messagesCtrl'
	}).when('/meetings', {
		templateUrl: 'static/partials/meetings.html',
		controller: 'MeetingsController',
		controllerAs: 'meetingsCtrl'
	}).when('/tasks', {
		templateUrl: 'static/partials/tasks.html',
		controller: 'TasksController',
		controllerAs: 'tasksCtrl'
	}).when('/teamManagement', {
		templateUrl: 'static/partials/teamManagement.html',
		controller: 'TeamManagementController',
		controllerAs: 'teamManagementCtrl'
	}).when('/teamPreferenceSurvey', {
		templateUrl: 'static/partials/teamPreferenceSurvey.html',
		controller: 'TeamPreferenceSurveyController',
		controllerAs: 'surveyCtrl'
	}).otherwise({
		redirectTo: '/'
	});
});
