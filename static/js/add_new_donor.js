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
$(function(){

  $('#newDonorForm').submit(function(e){
      e.preventDefault();
      $.ajax({
          url:'/add_new_user',
          type:'post',
          data:$('#newDonorForm').serialize(),
          success:function(){
              $('.alert-success').removeAttr('hidden');
              $('#newDonorForm')[0].reset();
          }
      });
  });
});



