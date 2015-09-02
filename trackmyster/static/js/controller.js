trackmysterApp.controller("homeCtrl", function($scope){

	$scope.title = "Home";

});

trackmysterApp.controller("liveMapCtrl", function($scope, busFactory){
	busFactory.getBusList().then(function(response){
		$scope.busList = response.data;
	})
	$scope.title = "Live Map";
  $scope.loc=[
      [18.638529,73.847787],
      [18.639231,73.840045],
      [18.637055,73.825679],
      [18.646896,73.814435]
    ];
})

trackmysterApp.controller("routeHistoryCtrl", function($scope){
	
	$scope.title = "Route History";
})
trackmysterApp.controller("attendanceCtrl", function($scope){
	
	$scope.title = "Attendance";
})