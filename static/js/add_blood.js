$(function () {
    $('#addbloodForm').submit(function (e) {
        e.preventDefault();
        data = $('#addbloodForm').serialize();
        $.ajax({
            url: '/add_blood',
            type: 'post',
            data: data,
            success: function () {
                $('#newDriveSuccess').removeAttr('hidden');
                $('#newDrive')[0].reset();
            },
            error: function () {
                $('#newDriveFailure').removeAttr('hidden');
            }
        });
    });
});