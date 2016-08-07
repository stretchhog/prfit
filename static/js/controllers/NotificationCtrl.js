app.controller('NotificationCtrl', [
	'$scope', '$sce', 'Notification',
	function ($scope, $sce, Notification) {
		const delay = 2500;
		$scope.primaryNotification = function (title, message) {
			Notification({title: title, message: message, delay: delay});
		};
		$scope.errorNotification = function (title, message) {
			Notification.error({title: title, message: message, delay: delay});
		};
		$scope.successNotification = function (title, message) {
			Notification.success({title: title, message: message, delay: delay});
		};
		$scope.infoNotification = function (title, message) {
			Notification.info({title: title, message: message, delay: delay});
		};
		$scope.warningNotification = function (title, message) {
			Notification.warning({title: title, message: message, delay: delay});
		};

		$scope.printAsHtml = function (body) {
			return $sce.trustAsHtml(body)
		};

		$scope.capitalizeFirstLetter = function (string) {
			return $.trim(string).charAt(0).toUpperCase() + $.trim(string).slice(1)
		};

	}
]);


