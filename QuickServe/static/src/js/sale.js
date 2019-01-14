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
        $("#modal-sale").modal("show");
      },
      success: function (data) {
        $("#modal-sale .modal-content").html(data.html_form);
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
          // alert("Sale Added!");
          $("#datatable-responsive tbody").html(data.html_sale_list);
          $("#modal-sale").modal("hide");
          // alert("Sale Added!");
         swal("Sale Added!", "Successfully!", "success");
         // swal({title: "Sweet!", text: "Here's a custom image.",  timer: 2000,  imageUrl: "thumbs-up.jpg"});
         if(data.sale_delete){
            swal("Sale Deleted!", "As Requested!", "success");
         }
        }
        else {
          $("#modal-sale .modal-content").html(data.html_form);
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

  // Create sale
  $(".js-create-sale").click(loadForm);
  $("#modal-sale").on("submit", ".js-sale-create-form", saveForm);

  // Update sale
  $("#datatable-responsive").on("click", ".js-update-sale", loadForm);
  $("#modal-sale").on("submit", ".js-sale-update-form", saveForm);

  // Delete sale
  $("#datatable-responsive").on("click", ".js-delete-sale", loadForm);
  $("#modal-sale").on("submit", ".js-sale-delete-form", saveForm);

});
