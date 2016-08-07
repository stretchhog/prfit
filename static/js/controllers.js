app.controller('DashboardCtrl', [
	'$scope', 'DashboardService',
	function ($scope, DashboardService) {

		DashboardService.getCurrentPRs().then(function (response) {
			$scope.data = response.data;
			$scope.data.prs.forEach((d) => {
				d.prs.forEach((pr) => {
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
				})
			})
		}).catch(function (response) {
		});

	}
]);

