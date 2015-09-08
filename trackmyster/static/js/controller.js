trackmysterApp.controller("homeCtrl", function($scope){

	$scope.title = "Home";

});

trackmysterApp.controller("liveMapCtrl", function($scope, busFactory){
	
  busFactory.getBusList().then(function(response){
		$scope.busList = response.data;
	})
	$scope.title = "Live Map";
  var loc=[
      [18.638529,73.847787],
      [18.639231,73.840045],
      [18.637055,73.825679],
      [18.646896,73.814435]
    ];
    
    var waypts = [];
    for(var i=1;i<loc.length-1;i++){
      waypts.push({
        location:loc[i].join(),
        stopover:false
      });
    }

    $scope.waypts= waypts;
    $scope.loc = loc;

  $scope.getBusRoute = function (bus) {
      console.log(bus);
  }

})
trackmysterApp.controller("routeHistoryCtrl", function($scope){
	
	$scope.title = "Route History";
})
trackmysterApp.controller("attendanceCtrl", function($scope){
	
	$scope.title = "Attendance";
})