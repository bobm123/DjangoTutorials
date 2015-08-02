/*global $ */

var initialize = function (navigator) {
    $('#id_login').on('click', function () {
        navigator.id.request();
        //navigator.id.doSomethingElse();
    });
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};