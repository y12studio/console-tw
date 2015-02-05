// Include app dependency on ngMaterial
angular.module('YourApp', ['ngMaterial', 'ngResource']).controller(
    "YourController", [
        '$scope',
        '$resource',
        function($scope, $resource) {

            $scope.foo = "hello console";

        }
    ]);
