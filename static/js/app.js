var app = angular.module("app", ['ngResource', 'ui-notification']);
app.config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});
