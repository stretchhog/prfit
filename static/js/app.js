var app = angular.module("app", ['ngResource', 'ui-notification', 'ngMaterial']);
app.config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});
