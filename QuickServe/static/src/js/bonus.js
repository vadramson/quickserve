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
        $("#modal-bonus").modal("show");
      },
      success: function (data) {
        $("#modal-bonus .modal-content").html(data.html_form);
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
          // alert("Bonus Added!");
          $("#datatable-responsive tbody").html(data.html_bonus_list);
          $("#modal-bonus").modal("hide");
          // alert("Bonus Added!");
         swal("Bonus Added!", "Successfully!", "success");
         // swal({title: "Sweet!", text: "Here's a custom image.",  timer: 2000,  imageUrl: "thumbs-up.jpg"});
         if(data.bonus_delete){
            swal("Bonus Deleted!", "As Requested!", "success");
         }
        }
        else {
          $("#modal-bonus .modal-content").html(data.html_form);
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

  // Create bonus
  $(".js-create-bonus").click(loadForm);
  $("#modal-bonus").on("submit", ".js-bonus-create-form", saveForm);

  // Update bonus
  $("#datatable-responsive").on("click", ".js-update-bonus", loadForm);
  $("#modal-bonus").on("submit", ".js-bonus-update-form", saveForm);

  // Delete bonus
  $("#datatable-responsive").on("click", ".js-delete-bonus", loadForm);
  $("#modal-bonus").on("submit", ".js-bonus-delete-form", saveForm);

});
