trackmysterApp.controller("homeCtrl", function($scope){

	$scope.title = "Home";

});

trackmysterApp.controller("liveMapCtrl", function($scope){

	$scope.title = "Live Map";
	$scope.map= {
      center: {
        latitude: 35.681382,
        longitude: 139.766084
      },
      options: {
        maxZoom: 20,
        minZoom: 3
      },
      zoom: 15,
      polylines: [
          {
              path: [
                  {
                      latitude: 35.67941788049046,
                      longitude: 139.75768089294434
                  },
                  {
                      latitude: 35.67793632362604,
                      longitude: 139.76341009140015
                  },
                  {
                      latitude: 35.680759972963095,
                      longitude: 139.76446151733398
                  },
                  {
                      latitude: 35.68130028953324,
                      longitude: 139.76555585861206
                  }
              ],
              stroke: {
                  color: '#6060FB',
                  weight: 4
              },
              editable: true,
              draggable: false,
              geodesic: false,
              visible: true
          },
          {
              path: [
                  {
                      latitude: 35.682572633455436,
                      longitude: 139.77615594863892
                  },
                  {
                      latitude: 35.681579161170134,
                      longitude: 139.77576971054077
                  },
                  {
                      latitude: 35.682502916505676,
                      longitude: 139.77373123168945
                  },
                  {
                      latitude: 35.67920872118891,
                      longitude: 139.77173566818237
                  }
              ],
              stroke: {
                  color: '#6060FB',
                  weight: 3
              },
              editable: true,
              draggable: true,
              geodesic: true,
              visible: true
          }
      ]
  }
})

trackmysterApp.controller("routeHistoryCtrl", function($scope){
	
	$scope.title = "Route History";
})
trackmysterApp.controller("attendanceCtrl", function($scope){
	
	$scope.title = "Attendance";
})

trackmysterApp.config(function (uiGmapGoogleMapApiProvider) {
    uiGmapGoogleMapApiProvider.configure({
        key: '',
        v: '3',
        libraries: 'weather,geometry,visualization'
    });
});