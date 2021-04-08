$(function () {
    $('#addbloodForm').submit(function (e) {
        e.preventDefault();
        data = $('#addbloodForm').serialize();
        $.ajax({
            url: '/add_blood',
            type: 'post',
            data: data,
            success: function () {
                $('#addbloodinSuccess').removeAttr('hidden');
                $('#addbloodForm')[0].reset();
            },
            error: function () {
                $('#addbloodinFailure').removeAttr('hidden');
            }
        });
    });
});