app.controller('DashboardCtrl', [
	'$scope', 'DashboardService',
	function ($scope, DashboardService) {

		DashboardService.getCurrentPRs().then(function (response) {
			$scope.data = response.data;
			augmentData($scope.data)
		}).catch(function (response) {
		});

		function augmentData(data) {
			$scope.data.prs.forEach((d) => {
				d.prs.forEach((pr) => {
					addMetricIcon(pr);
					addUnits(pr)
				})
			})
		}
		function addMetricIcon(pr) {
			switch (pr.metric) {
				case "Time":
					pr.icon = Metrics.time;
					break;
				case "Distance":
					pr.icon = Metrics.distance;
					break;
				case "AMRAP":
					pr.icon = Metrics.amrap;
					break;
				case "One Rep Max":
					pr.icon = Metrics.weight;
					break;
			}
		}
		function addUnits(pr) {
			var units = Units.metric;
			switch (pr.metric) {
				case "Distance":
					pr.unit = units.distance;
					break;
				case "One Rep Max":
					pr.unit = units.weight;
					break;
			}
		}
	}
]);

