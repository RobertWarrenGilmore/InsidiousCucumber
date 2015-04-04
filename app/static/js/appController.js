/**
 * The App Controller which acts as a global controller for the main HTML
 * template and all page elements.  It controls many aspects that need to
 * be on each page such as user information.
 */

var app = angular.module('minerva', ['ngRoute', 'ui.bootstrap']);

/*GLOBAL CONTROLLER*/
app.controller('AppController', function() {
	console.log("Creating App Controller");

	var self = this;

	self.user = {fname:'Wayne', lname:'Starr', professor:true}
});