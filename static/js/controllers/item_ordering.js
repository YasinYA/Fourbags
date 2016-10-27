angular.module('FourBags')
    .controller('OrderController', ['$scope', 'OrderService', function($scope, OrderService){
        $scope.sendOrder = function() {
            $scope.customer.item = window.item;

            // Post order detials
            result = OrderService.sentItemOrder($scope.customer);
            result.then(function(res){
                if(res.data.success) {
                    $scope.sucessfull = true;
                    $scope.successMessage = "Your Order is Sucessfull";
                }
            });
        };
    }]);
