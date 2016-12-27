angular.module('FourBags')
    .controller('ItemController', ['$scope', function($scope){
        $scope.items = window.items;

        $scope.filterBySearchTerm = function(term) {
            $scope.searched = term;
        };
        console.log($scope.items);
    }]);
