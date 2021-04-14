$(function () {
  $("#newOrgForm").submit(function (e) {
    e.preventDefault();
    $.ajax({
      url: "/add_new_org",
      type: "post",
      data: $("#newOrgForm").serialize(),
      success: function () {
        $("#newOrgSuccess").removeAttr("hidden");
        $("#newOrgForm")[0].reset();
      },
      error: function () {
        $("#newOrgFailure").removeAttr("hidden");
        $("#newOrgForm")[0].reset();
      },
    });
  });
});
