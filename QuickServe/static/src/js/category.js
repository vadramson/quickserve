$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-category").modal("show");
      },
      success: function (data) {
        $("#modal-category .modal-content").html(data.html_form);
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
          $("#datatable-responsive tbody").html(data.html_category_list);
          $("#modal-category").modal("hide");
        }
         if(data.category_activate){
            swal("Category Activate!", "Successfully!", "success");
         }
         if(data.category_deactivate){
            swal("Category Deactivate!", "As Requested!", "success");
         }
         if(data.save_category){
            swal("Category Added!", "Successfully!", "success");
         }
         if(data.save_category_error){
            swal("Unknown Error!", "Occurred!", "error");
         }
        else {
          $("#modal-category .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create category
  $(".js-create-category").click(loadForm);
  $("#modal-category").on("submit", ".js-category-create-form", saveForm);

  // Update category
  $("#datatable-responsive").on("click", ".js-update-category", loadForm);
  $("#modal-category").on("submit", ".js-category-update-form", saveForm);

   // Deactivate category
  $("#datatable-responsive").on("click", ".js-deactivate-category", loadForm);
  $("#modal-category").on("submit", ".js-category-deactivate-form", saveForm);

  // Activate category
  $("#datatable-responsive").on("click", ".js-activate-category", loadForm);
  $("#modal-category").on("submit", ".js-category-activate-form", saveForm);

});
