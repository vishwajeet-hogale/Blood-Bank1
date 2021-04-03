$(function(){
    $('#patLoginForm').submit(function(e){
        //e.preventDefault();
        $.ajax({
            url:'/pat_login',
            type:'post',
            data:$('#patLoginForm').serialize(),
            success:function(){
                $('#patLoginSuccess').removeAttr('hidden');
                $('#patLoginForm')[0].reset();
            },
            error:function(){
                $('#patLoginFailure').removeAttr('hidden');
            }
        });
    });
  $('#newOrgForm').submit(function(e){
      e.preventDefault();
      $.ajax({
          url:'/add_new_org',
          type:'post',
          data:$('#newOrgForm').serialize(),
          success:function(){
              $('#newOrgSuccess').removeAttr('hidden');
              $('#newOrgForm')[0].reset();
          },
          error:function(){
              $('#newOrgFailure').removeAttr('hidden');
          }
      });
  });

  $('#orgLoginForm').submit(function(e){
      //e.preventDefault();
      $.ajax({
          url:'/org_login',
          type:'post',
          data:$('#orgLoginForm').serialize(),
          success:function(){
              $('#orgLoginSuccess').removeAttr('hidden');
              $('#orgLoginForm')[0].reset();
          },
          error:function(){
              $('#orgLoginFailure').removeAttr('hidden');
          }
      });
  });
  
});



