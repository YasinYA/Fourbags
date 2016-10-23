angular.module('FourBags')
    .controller('OrderController', ['$scope', function($scope){
        $scope.sendOrder = function() {
            console.log($scope.customer);
        };
    }]);
