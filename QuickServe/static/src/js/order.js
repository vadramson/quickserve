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
        $("#modal-order").modal("show");
      },
      success: function (data) {
        $("#modal-order .modal-content").html(data.html_form);
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
          // alert("Order Added!");
          $("#datatable-responsive tbody").html(data.html_order_list);
          $("#modal-order").modal("hide");
          // alert("Order Added!");
         swal("Product Added!", "To Cart!", "success");
         // swal({title: "Sweet!", text: "Here's a custom image.",  timer: 2000,  imageUrl: "thumbs-up.jpg"});
        }
         if(data.insufficient_product){
          $("#datatable-responsive tbody").html(data.html_order_list);
          // alert(" Employee Code does Not Exists! ");
            swal("Insufficient Product!", "in Stock, Reduce quantity and try again!", "error");
         }
        if(data.order_delete){
          $("#datatable-responsive tbody").html(data.html_order_list);
          $("#modal-order").modal("hide");
            swal("Product Remove!", "From Cart!", "success");
         }
        else {
          $("#modal-order .modal-content").html(data.html_form);

        }

      },
      error: function(data) {
        swal("Unknown Error Occurred", "May be Due To Invalid Form!", "error");
    }
    });
    return false;
  };


  /* Binding */

  // Create order

  $(".js-create-order").click(loadForm);
  $("#modal-order").on("submit", ".js-order-create-form", saveForm);



  // Delete order
  $("#datatable-responsive").on("click", ".js-delete-order", loadForm);
  $("#modal-order").on("submit", ".js-order-delete-form", saveForm);

});
