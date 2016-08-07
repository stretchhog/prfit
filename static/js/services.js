app.factory('DashboardService', function ($http) {

	var service = {};

	service.getCurrentPRs = function () {
		return $http({
			method: 'GET',
			url: 'api/current_prs'
		}).then(function successCallback(response) {
			return response;
			// this callback will be called asynchronously
			// when the response is available
		}, function errorCallback(response) {
			// called asynchronously if an error occurs
			// or server returns response with an error status.
		})
	};

	return service
});

