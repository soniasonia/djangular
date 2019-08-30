(function () {
    'use strict';

    angular.module('scrumboard.demo')
        .directive('scrumboardCard', CardDirective);

    function CardDirective() {
        return {
            templateUrl: '/static/scrumboard_app/card.html',
            restrict: 'E',
            // Adding controller to directive (implement update function to send update to backend)
            // Controller is represented by a list, first items in the list are dependencies (by string)

            controller: ['$scope', '$http', function ($scope, $http) {
                var url = '/scrumboard/cards/' + $scope.card.id + '/';

                $scope.update = function () {
                    $http.put(url, $scope.card);
                };

                $scope.delete = function() {
                    $http.delete(url).then(
                        function(){
                            var cards = $scope.list.cards;
                            cards.splice(indexOf($scope.card), 1);
                        }
                    )
                };

                $scope.modelOptions = {
                    debounce: 500
                };
                // so it does not update after every keystroke
                // it wait 500ms wait for next vhange after sending update to backend
            }]
        }
    }
})();