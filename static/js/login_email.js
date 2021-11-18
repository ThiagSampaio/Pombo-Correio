$(document).ready(function () {
    $(document).on('submit', '#email-form', function (e) {
        e.preventDefault();
        req = $.ajax({
            url: '/login',
            type: 'GET',
            data: {
                email: $("#email").val(),
                senha: $("#senha").val()
            },
        });
    });
});