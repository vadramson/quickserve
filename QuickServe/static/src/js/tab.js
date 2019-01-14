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
        $("#modal-tab").modal("show");
      },
      success: function (data) {
        $("#modal-tab .modal-content").html(data.html_form);
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
          // alert("Tab Added!");
          $("#datatable-responsive tbody").html(data.html_tab_list);
          $("#modal-tab").modal("hide");
          // alert("Tab Added!");
         swal("New Tab Created!", "Successfully!", "success");
         // swal({title: "Sweet!", text: "Here's a custom image.",  timer: 2000,  imageUrl: "thumbs-up.jpg"});
        }
        if(data.tab_delete){
          $("#datatable-responsive tbody").html(data.html_tab_list);
          $("#modal-tab").modal("hide");
            swal("Product Remove!", "From Cart!", "success");
         }
        else {
          $("#modal-tab .modal-content").html(data.html_form);

        }

      },
      error: function() {
        swal("Unknown Error Occurred", "May be Due To Invalid Form!", "error");
    }
    });
    return false;
  };


  /* Binding */

  // Create tab
  $(".js-create-tab").click(loadForm);
  $("#modal-tab").on("submit", ".js-tab-create-form", saveForm);

  $(".js-create-tab").click(loadForm);
  $("#modal-tab").on("submit", ".js-tab-create-form", saveForm);

  // Delete tab
  $("#datatable-responsive").on("click", ".js-delete-tab", loadForm);
  $("#modal-tab").on("submit", ".js-tab-delete-form", saveForm);

});
