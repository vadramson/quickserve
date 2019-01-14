$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-expense").modal("show");
      },
      success: function (data) {
        $("#modal-expense .modal-content").html(data.html_form);
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
          $("#datatable-responsive tbody").html(data.html_expense_list);
          $("#modal-expense").modal("hide");
        }
        else {
          $("#modal-expense .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create expense
  $(".js-create-expense").click(loadForm);
  $("#modal-expense").on("submit", ".js-expense-create-form", saveForm);

  // Update expense
  $("#datatable-responsive").on("click", ".js-update-expense", loadForm);
  $("#modal-expense").on("submit", ".js-expense-update-form", saveForm);

  // Delete expense
  $("#datatable-responsive").on("click", ".js-delete-expense", loadForm);
  $("#modal-expense").on("submit", ".js-expense-delete-form", saveForm);

});
