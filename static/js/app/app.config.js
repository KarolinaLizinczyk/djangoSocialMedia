/**
 * Created by Jacob on 2017-10-19.
 */
"use strict";

angular.module('app').config(function ($interpolateProvider){
    $interpolateProvider.startSymbol('//');
    $interpolateProvider.endSymbol('//');
});
