$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-department").modal("show");
      },
      success: function (data) {
        $("#modal-department .modal-content").html(data.html_form);
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
          $("#datatable-responsive tbody").html(data.html_department_list);
          $("#modal-department").modal("hide");
        }
        else {
          $("#modal-department .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create department
  $(".js-create-department").click(loadForm);
  $("#modal-department").on("submit", ".js-department-create-form", saveForm);

  // Update department
  $("#datatable-responsive").on("click", ".js-update-department", loadForm);
  $("#modal-department").on("submit", ".js-department-update-form", saveForm);

  // Delete department
  $("#datatable-responsive").on("click", ".js-delete-department", loadForm);
  $("#modal-department").on("submit", ".js-department-delete-form", saveForm);

});
