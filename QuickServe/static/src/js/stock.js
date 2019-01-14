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
        $("#modal-stocks").modal("show");
      },
      success: function (data) {
        $("#modal-stocks .modal-content").html(data.html_form);
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
          // alert("Stocks Added!");
          $("#datatable-responsive tbody").html(data.html_stocks_list);
          $("#modal-stocks").modal("hide");
          // alert("Stocks Added!");
         swal("Stocks Added!", "Successfully!", "success");
         // swal({title: "Sweet!", text: "Here's a custom image.",  timer: 2000,  imageUrl: "thumbs-up.jpg"});
         if(data.stocks_delete){
            swal("Stocks Deleted!", "As Requested!", "success");
         }
        }
        else {
          $("#modal-stocks .modal-content").html(data.html_form);
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

  // Create stocks
  $(".js-create-stocks").click(loadForm);
  $("#modal-stocks").on("submit", ".js-stocks-create-form", saveForm);

  // Update stocks
  $("#datatable-responsive").on("click", ".js-update-stocks", loadForm);
  $("#modal-stocks").on("submit", ".js-stocks-update-form", saveForm);

  // Delete stocks
  $("#datatable-responsive").on("click", ".js-delete-stocks", loadForm);
  $("#modal-stocks").on("submit", ".js-stocks-delete-form", saveForm);

});
