(function () {
'use strict';

angular.module('scrumboard.demo')
    .config(['$routeProvider', config])
    .run(['$http', run]);

    function config($routeProvider){
        $routeProvider
            .when('/', {
                templateUrl: '/static/html/scrumboard.html',
                controller: 'ScrumboardController',
            })
            .when('/login', {
                templateUrl : '/static/html/login.html',
                controller: 'LoginController'
            })
            .otherwise('/');
    }

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
})();

// Retrieve scrumboard mode, run function "run"
// Custom run function in run function
// Any function pass to angular run function is executed when application starts (after modules are loaded)