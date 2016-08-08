var app = angular.module("app", ['ngResource']);
app.config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});
