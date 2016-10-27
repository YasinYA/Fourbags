angular.module('FourBags')
    .service('OrderService', ['$http', function($http){
        this.sentItemOrder = function(data) {
            return $http.post('/order/', data).then(function(res) {
                return res;
            }, function(err) {
                return err;
            });
        };
    }]);
