$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-loss").modal("show");
      },
      success: function (data) {
        $("#modal-loss .modal-content").html(data.html_form);
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
          $("#datatable-responsive tbody").html(data.html_loss_list);
          $("#modal-loss").modal("hide");
        }
        else {
          $("#modal-loss .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create loss
  $(".js-create-loss").click(loadForm);
  $("#modal-loss").on("submit", ".js-loss-create-form", saveForm);

  // Update loss
  $("#datatable-responsive").on("click", ".js-update-loss", loadForm);
  $("#modal-loss").on("submit", ".js-loss-update-form", saveForm);

  // Delete loss
  $("#datatable-responsive").on("click", ".js-delete-loss", loadForm);
  $("#modal-loss").on("submit", ".js-loss-delete-form", saveForm);

});
