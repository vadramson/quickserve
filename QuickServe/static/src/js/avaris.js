$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-avaris").modal("show");
      },
      success: function (data) {
        $("#modal-avaris .modal-content").html(data.html_form);
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
        if (data.form_is_valid) {
          $("#datatable-responsive tbody").html(data.html_avaris_list);
          $("#modal-avaris").modal("hide");
          swal("Avaris Registered ", "Successfully!", "success");
        }
         if(data.avaris_update){
            swal("Avaris Updated ", "Successfully!", "success");
         }
         if(data.form_not_valid){
            swal("Invalid Form!", "Try Again!", "success");
         }
        else {
          $("#modal-avaris .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create avaris
  $(".js-create-avaris").click(loadForm);
  $("#modal-avaris").on("submit", ".js-avaris-create-form", saveForm);

  // Update avaris
  $("#datatable-responsive").on("click", ".js-update-avaris", loadForm);
  $("#modal-avaris").on("submit", ".js-avaris-update-form", saveForm);

  // Delete avaris
  $("#datatable-responsive").on("click", ".js-delete-avaris", loadForm);
  $("#modal-avaris").on("submit", ".js-avaris-delete-form", saveForm);

});
