$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-purchase").modal("show");
      },
      success: function (data) {
        $("#modal-purchase .modal-content").html(data.html_form);
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
          $("#datatable-responsive tbody").html(data.html_purchase_list);
          $("#modal-purchase").modal("hide");
          swal("Purchase Registered ", "Successfully!", "success");
        }
         if(data.purchase_update){
            swal("Purchase Updated ", "Successfully!", "success");
         }
         if(data.form_not_valid){
            swal("Invalid Form!", "Try Again!", "success");
         }
        else {
          $("#modal-purchase .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create purchase
  $(".js-create-purchase").click(loadForm);
  $("#modal-purchase").on("submit", ".js-purchase-create-form", saveForm);

  // Update purchase
  $("#datatable-responsive").on("click", ".js-update-purchase", loadForm);
  $("#modal-purchase").on("submit", ".js-purchase-update-form", saveForm);

  // Delete purchase
  $("#datatable-responsive").on("click", ".js-delete-purchase", loadForm);
  $("#modal-purchase").on("submit", ".js-purchase-delete-form", saveForm);

});
