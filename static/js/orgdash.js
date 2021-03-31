$(function(){

  $.ajax({
      url:'/get_alert',
      type:'post',
      data:"",
      async: true,
      success:function(msg){
        var count = msg['count'];
        var r = "record";
        for (var i=0;i<count;i++){
          $("#alertTable").append("<tr><td class='body-item mbr-fonts-style display-7'>"+msg[r+i]['type']+"</td><td class='body-item mbr-fonts-style display-7'>"+msg[r+i]['location']+"</td><td class='body-item mbr-fonts-style display-7'>"+msg[r+i]['priority']+"</td><td class='body-item mbr-fonts-style display-7'>"+msg[r+i]['phone']+"</td></tr>");
        }
      }
  });

  $.ajax({
      url:'/get_donors',
      type:'post',
      data:"",
      async: true,
      success:function(msg){
        var count = msg['count'];
        var r = "record";
        for (var i=0;i<count;i++){
          $("#donorTable").append("<tr><td class='body-item mbr-fonts-style display-7'>"+msg[r+i]['name']+"</td><td class='body-item mbr-fonts-style display-7'>"+msg[r+i]['email']+"</td><td class='body-item mbr-fonts-style display-7'>"+msg[r+i]['phone']+"</td><td class='body-item mbr-fonts-style display-7'>"+msg[r+i]['bloodgroup']+"</td></tr>");
        }
      }
  });

  $.ajax({
      url:'/get_drive',
      type:'post',
      data:"",
      async: true,
      success:function(msg){
        var count = msg['count'];
        var r = "record";
        for (var i=0;i<count;i++){
          $("#driveTable").append("<tr><td class='body-item mbr-fonts-style display-7'>"+msg[r+i]['name']+"</td><td class='body-item mbr-fonts-style display-7'>"+msg[r+i]['phone']+"</td><td class='body-item mbr-fonts-style display-7'>"+msg[r+i]['location']+"</td></tr>");
        }
      }
  });

  $('#newAlert').submit(function(e){
      e.preventDefault();
      email = $('#email_div').data('email');
      data = $('#newAlert').serialize();
      data['email'] = email;
      $.ajax({
          url:'/add_new_alert',
          type:'post',
          data:data,
          success:function(){
              $('#newAlertSuccess').removeAttr('hidden');
              $('#newAlert')[0].reset();
          },
          error:function(){
              $('#newAlertFailure').removeAttr('hidden');
          }
      });
  });

  $('#newDrive').submit(function(e){
      e.preventDefault();
      data = $('#newDrive').serialize();
      $.ajax({
          url:'/add_new_drive',
          type:'post',
          data:data,
          success:function(){
              $('#newDriveSuccess').removeAttr('hidden');
              $('#newDrive')[0].reset();
          },
          error:function(){
              $('#newDriveFailure').removeAttr('hidden');
          }
      });
  });

});
