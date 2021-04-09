$(function () {
    $('#subtractbloodForm').submit(function (e) {
        e.preventDefault();
        data = $('#subtractbloodForm').serialize();
        $.ajax({
            url: '/subtract_blood',
            type: 'post',
            data: data,
            success: function () {
                $('#subtractbloodinSuccess').removeAttr('hidden');
                $('#subtractbloodForm')[0].reset();
            },
            error: function () {
                $('#subtractbloodinFailure').removeAttr('hidden');
            }
        });
    });
});