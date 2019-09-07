(function () {
    'use strict';

    angular.module('scrumboard.demo')
        .directive('scrumboardCard', CardDirective);

    function CardDirective() {
        return {
            templateUrl: '/static/html/card.html',
            restrict: 'E',
            // Adding controller to directive (implement update function to send update to backend)
            // Controller is represented by a list, first items in the list are dependencies (by string)

            controller: ['$scope', '$http', function ($scope, $http) {
                var url = '/scrumboard/cards/' + $scope.card.id + '/';
                $scope.destList = $scope.list;


                $scope.update = function () {
                    return $http.put(
                    url,
                    $scope.card
                    );
                };

                $scope.delete = function() {
                    $http.delete(url).then(
                        function(){
                            var cards = $scope.list.cards;
                            cards.splice(cards.indexOf($scope.card),
                            1
                            );
                        }
                    );
                };

                $scope.modelOptions = {
                    debounce: 500
                };

                $scope.move = function () {
                    if ($scope.destList === undefined) {
                        return;
                        }
                        $scope.card.list = $scope.destList.id;
                        $scope.update().then(function () {
                            {
                                removeCardFromList($scope.card, $scope.list);
                                $scope.destList.cards.push($scope.card);
                            }
                    });
                }
                // so it does not update after every keystroke
                // it wait 500ms wait for next vhange after sending update to backend
            }]
        }
    }
})();