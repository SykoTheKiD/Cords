angular
  .module('myApp',['ngMaterial'])
  .controller('GridCtrl', ['$scope', function ($scope) {
    $scope.grid = [[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13], [13,14,15,16]];
  }]);