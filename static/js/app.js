
var htmedia = angular.module('htMedia', [])
.config(function($interpolateProvider, $httpProvider) {
  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
})
.controller('htCtrl', function($scope, $http) {
  $scope.getrange = function(n) {
    return new Array(n);
  };
  $scope.mnstate = '';
  $scope.electionyear = ''; 
  $scope.mynetastate = myneta_data;
  $scope.winner_data = [];
  $scope.show_loading = false;

  $scope.no_data = false; 
  $scope.get_winner_data = function() {
    $scope.no_data = false; 
    $scope.winner_data = [];
    console.log($scope.mnstate, $scope.electionyear);
    if(!$scope.mnstate || !$scope.electionyear) {
      return false;
    }
    $scope.show_loading = true;
    $scope.url = window.location.origin + '/mynetaapi?state=' + $scope.mnstate +'&year=' +$scope.electionyear; 
    $http.get('/mynetaapi?state=' + $scope.mnstate +'&year=' +$scope.electionyear).
      success(function(data) {
        $scope.show_loading = false;
        $scope.winner_data = data.data;
        if(!data.data.length) {
          $scope.no_data = true;
        }
      });  
  };
});
