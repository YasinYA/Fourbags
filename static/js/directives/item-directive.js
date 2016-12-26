angular.module('FourBags')
    .directive('itemdirective', function(){
        return {
            $scope: {},
            restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
            template: '<pre>{$ hello $}</pre>',
            link: function($scope, iElm, iAttrs) {
                $scope.hello = iAttrs.item;
                // console.log($scope.hello);
            }
        };
    });
