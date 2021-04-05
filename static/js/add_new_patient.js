$(function(){
    $('#newPatientForm').submit(function(e){
        e.preventDefault();
        $.ajax({
            url:'/add_new_patient',
            type:'post',
            data:$('#newPatientForm').serialize(),
            success:function(){
                $('.alert-success').removeAttr('hidden');
                $('#newPatientForm')[0].reset();
            }
        });
    });
  });