$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-menu").modal("show");
      },
      success: function (data) {
        var mu = $("#modal-menu .modal-content").html(data.html_form);
        console.log('menu now ');
        console.log(mu);
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
          $("#datatable-responsive tbody").html(data.html_menu_list);
          $("#modal-menu").modal("hide");
        }
        else {
          $("#modal-menu .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create menu
  $(".js-create-menu").click(loadForm);
  $("#modal-menu").on("submit", ".js-menu-create-form", saveForm);

  // Update menu
  $("#datatable-responsive").on("click", ".js-update-menu", loadForm);
  $("#modal-menu").on("submit", ".js-menu-update-form", saveForm);

  // Delete menu
  $("#datatable-responsive").on("click", ".js-delete-menu", loadForm);
  $("#modal-menu").on("submit", ".js-menu-delete-form", saveForm);

});
