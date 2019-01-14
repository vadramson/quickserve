$(function () {
// alert("Book created!");
  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-attendance").modal("show");
      },
      success: function (data) {
        $("#modal-attendance .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        // alert("Book created 2 !");
        if (data.form_is_valid) {
          // alert("Attendance Added!");
          $("#datatable-responsive tbody").html(data.html_attendance_list);
          $("#modal-attendance").modal("hide");
                  
         if(data.attendance_clockin){
            swal("Cloked In.!", "Your Meter starts Running Now...", "success");
         }
		 
         if(data.attendance_clockin_err){
            swal("Already Clocked in", "Can't Clock in twice per day", "error");
         }
		 
		 if(data.attendance_clockout){
            swal("Clocked Out.!", "You have clocked out for the day", "success");
         }
		 
         if(data.attendance_clockin_err){
            swal("Already Clocked in", "Can't Clock in twice per day", "error");
         }
		 
        }
        else {
          $("#modal-attendance .modal-content").html(data.html_form);
          swal("Invalid Code", "Employee Code does Not Exists!", "error");
          // alert(" Employee Code does Not Exists! ");
        }
      },
      error: function(data) {
        alert(" Unknown Error Occurred! ");
    }
    });
    return false;
  };


  /* Binding */

  // Create attendance
  $(".js-create-attendance").click(loadForm);
  $("#modal-attendance").on("submit", ".js-attendance-create-form", saveForm);

  // Update attendance
  $(".js-update-attendance").click(loadForm);
  $("#modal-attendance").on("submit", ".js-attendance-update-form", saveForm);

  // Delete attendance
  $("#datatable-responsive").on("click", ".js-delete-attendance", loadForm);
  $("#modal-attendance").on("submit", ".js-attendance-delete-form", saveForm);

});
