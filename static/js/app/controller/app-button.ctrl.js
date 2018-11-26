/**
 * Created by Jacob on 2017-10-19.
 */
"use strict";


app.controller('myCtrl', function($scope) {
    $scope.count = 0;
    console.log("Hello")
    $scope.clicked = function () {
        $scope.count++;

    }
});
