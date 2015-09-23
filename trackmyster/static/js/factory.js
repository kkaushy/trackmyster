trackmysterApp.factory('studentFactory', function($http){
	var urlBase = '/api/student/';
	var _studentService = {};

	_studentService.getStudents = function(studentId){
		if(studentId){			
			return $http.get(urlBase+studentId);
		}
		return $http.get(urlBase);
	}

	_studentService.createStudent = function(Student){
		return $http.post(urlBase, Student);
	}

	_studentService.deleteStudent = function(Student){
		return $http.delete(urlBase+Student.id);
	}
	

	return _studentService;
});

trackmysterApp.factory('busFactory', function($http){
	var urlBase = '/api/bus/';
	var _busService = {};

	_busService.getBusList = function(busId){
		if(busId)
			return $http.get(urlBase+busId);
		return $http.get(urlBase);
	}

	_busService.createBus = function(Bus){
		return $http.post(urlBase, Bus);
	}

	return _busService;
});

// trackmysterApp.factory('categoryFactory', function($http){
// 	var urlBase = '/api/category';
// 	var _categoryService = {};

// 	_categoryService.getCategories = function(){
// 		return $http.get(urlBase);
// 	}
// 	return _categoryService;
// });

// trackmysterApp.factory('employeeFactory', function($http){
// 	var urlBase = '/api/employee';
// 	var _employeeService = {};

// 	_employeeService.getEmployee = function(empId){
// 		if(empId){
// 			return $http.get(urlBase+"/"+empId);
// 		}
// 		return $http.get(urlBase);
// 	}
// 	return _employeeService;
// });