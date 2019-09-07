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

//retrieve scrumboard mode, run function "run"
//custom run function in run function
// any function pass to angular run function is executed when application starts (alfter modules are loaded)