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
        $("#modal-deduction").modal("show");
      },
      success: function (data) {
        $("#modal-deduction .modal-content").html(data.html_form);
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
          // alert("Deduction Added!");
          $("#datatable-responsive tbody").html(data.html_deduction_list);
          $("#modal-deduction").modal("hide");
          // alert("Deduction Added!");
         swal("Deduction Added!", "Successfully!", "success");
         // swal({title: "Sweet!", text: "Here's a custom image.",  timer: 2000,  imageUrl: "thumbs-up.jpg"});
         if(data.deduction_delete){
            swal("Deduction Deleted!", "As Requested!", "success");
         }
        }
        else {
          $("#modal-deduction .modal-content").html(data.html_form);
          swal("Invalid Code", "Employee Code does Not Exists!", "error");
          // alert(" Employee Code does Not Exists! ");
        }
      },
      error: function(data) {
        alert(" Employee Code does Not Exists! ");
    }
    });
    return false;
  };


  /* Binding */

  // Create deduction
  $(".js-create-deduction").click(loadForm);
  $("#modal-deduction").on("submit", ".js-deduction-create-form", saveForm);

  // Update deduction
  $("#datatable-responsive").on("click", ".js-update-deduction", loadForm);
  $("#modal-deduction").on("submit", ".js-deduction-update-form", saveForm);

  // Delete deduction
  $("#datatable-responsive").on("click", ".js-delete-deduction", loadForm);
  $("#modal-deduction").on("submit", ".js-deduction-delete-form", saveForm);

});
