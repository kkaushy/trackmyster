trackmysterApp = angular.module('trackmysterApp',['ui.router','daterangepicker','google-maps']).
	config(function($stateProvider, $urlRouterProvider){

	  $urlRouterProvider.otherwise("");	  
	  $stateProvider
	    .state('home', {
	      url: "",
	      templateUrl: "/static/partials/home.html",
	      controller:'homeCtrl'
	    })
	    .state('livemap', {
	      url: "2",
	      templateUrl: "/static/partials/livemap.html",
	      controller:'liveMapCtrl'
	    })
	    .state('routehistory', {
	      url: "3",
	      templateUrl: "/static/partials/routehistory.html",
	      controller:'routeHistoryCtrl'
	    })
	    .state('attendance', {
	      url: "4",
	      templateUrl: "/static/partials/attendance.html",
	      controller:'attendanceCtrl'
	    })
	});