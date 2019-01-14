$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-product").modal("show");
      },
      success: function (data) {
        $("#modal-product .modal-content").html(data.html_form);
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
          swal("Product Added!", "Successfully!", "success");
          $("#datatable-responsive tbody").html(data.html_product_list);
          $("#modal-product").modal("hide");
        }
        if(data.product_activate){
            swal("Product Activated !", "Successfully!", "success");
         }
         if(data.product_deactivate){
            swal("Product Deactivated !", "Successfully!", "success");
         }
         if(data.form_error){
            swal("Unknown Error !", "Occurred!", "error");
         }
        else {
          $("#modal-product .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create product
  $(".js-create-product").click(loadForm);
  $("#modal-product").on("submit", ".js-product-create-form", saveForm);

  // Update product
  $("#datatable-responsive").on("click", ".js-update-product", loadForm);
  $("#modal-product").on("submit", ".js-product-update-form", saveForm);

  // Activate product
  $("#datatable-responsive").on("click", ".js-activate-product", loadForm);
  $("#modal-product").on("submit", ".js-product-activate-form", saveForm);

   // Deactivate product
  $("#datatable-responsive").on("click", ".js-deactivate-product", loadForm);
  $("#modal-product").on("submit", ".js-product-deactivate-form", saveForm);

});
