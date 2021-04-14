$(function () {
    $('#newUpdateForm').submit(function (e) {
        e.preventDefault();
        data = $('#newUpdateForm').serialize();
        $.ajax({
            url: '/update',
            type: 'post',
            data: $("#newUpdateForm").serialize(),
            success: function () {
                $('.alert-success').removeAttr('hidden');
                $('#newUpdateForm')[0].reset();
            },
            error: function () {
                $('.alert-danger').removeAttr('hidden');
            }
        });
    });
});