$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-agency").modal("show");
      },
      success: function (data) {
        $("#modal-agency .modal-content").html(data.html_form);
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
          $("#datatable-responsive tbody").html(data.html_agency_list);
          $("#modal-agency").modal("hide");
        }
        else {
          $("#modal-agency .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create agency
  $(".js-create-agency").click(loadForm);
  $("#modal-agency").on("submit", ".js-agency-create-form", saveForm);

  // Update agency
  $("#datatable-responsive").on("click", ".js-update-agency", loadForm);
  $("#modal-agency").on("submit", ".js-agency-update-form", saveForm);

  // Delete agency
  $("#datatable-responsive").on("click", ".js-delete-agency", loadForm);
  $("#modal-agency").on("submit", ".js-agency-delete-form", saveForm);

});
