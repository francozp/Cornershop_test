$(function () {
  $("#datetimepicker1").datetimepicker({
    defaultDate: new Date(),
    format: 'DD/MM/YYYY',
  });
});

  
var dishesQty = 1;

$(document).ready(function(){
  $('#id_form-INITIAL_FORMS').val(1);
  var uniqueProducts = function(prod){
    var value;
    var seenOnce = false;
    for (var i = 0; i <= dishesQty; i++) {
      value = $('#id_form-'+i+'-maindish').val();
      console.log(value)
      if (!isNaN(value) && value.length !== 0) {
        if (value == prod){
          if (seenOnce){
            return false;
          } else {
            seenOnce = true;
          }
        }
      }
    }
    return true;
  };

$('#id_form-0-maindish').selectize({
  valueField: 'description',
  labelField: 'description',
  searchField: 'description',
  preload: true,
  create: false,
  options: [],
  load: function(query, callback) {
  $.ajax({
      url: "api/getdishes",
      type: 'GET',
      dataType: 'json',
      error: function() {
          callback();
      },
      success: function(res) {
        callback(res);
      }
    });
  },
  onChange: function (value) {
    if(!uniqueProducts(value)){
      $(this)[0].clear();
      $.notify({
        icon: 'mdi mdi-cancel',
        title: "Error",
        message: "No se permite repetir Platos Principales."
        },{
        element: '#tablaOpciones',
        type: "danger",
        clickToHide: true,
        autoHide: true,
        autoHideDelay: 100,
        showAnimation: 'slideDown',
        showDuration: 400,
        hideAnimation: 'slideUp',
        hideDuration: 200
      });
    }
  }
});



$('.add_option').click(function(){
var idt = parseInt($('#tablaOpciones tr:last').attr('id')) + 1;
var option = idt+1;
var lastMain = $('#id_form-'+(idt-1)+'-maindish').val();
if (lastMain != "") {
  $('#tablaOpciones tr:last').after(`
  <tr id="`+idt+`">
    <td style="text-align: center">
        ` + option + `
    </td>
    <td>
        <select name="form-`+idt+`-maindish" id="id_form-`+idt+`-maindish"></select>
    </td>
    <td style="text-align: center">
        <input type="checkbox" name="form-`+idt+`-salad" id="id_form-`+idt+`-salad">
    </td>
    <td style="text-align: center">
        <input type="checkbox" name="form-`+idt+`-dessert" id="id_form-`+idt+`-dessert">
    </td>
</tr>
  `);
  $('#id_form-'+idt+'-maindish').selectize({
    valueField: 'description',
    labelField: 'description',
    searchField: 'description',
    preload: true,
    create: false,
    options: [],
    load: function(query, callback) {
      $.ajax({
          url: "api/getdishes",
          type: 'GET',
          dataType: 'json',
          error: function() {
              callback();
          },
          success: function(res) {
            callback(res);
          }
        });
      },
    onChange: function (value) {
      if(!uniqueProducts(value)){
        $(this)[0].clear();
        $.notify({
          icon: 'mdi mdi-cancel',
          title: "Error",
          message: "No se permite repetir Platos Principales."
          },{
          element: '#tablaOpciones',
          type: "danger",
          clickToHide: true,
          autoHide: true,
          autoHideDelay: 100,
          showAnimation: 'slideDown',
          showDuration: 400,
          hideAnimation: 'slideUp',
          hideDuration: 200
        });
      }
    }
  })
}

else{
  $(`<div class="alert alert-warning alert-dismissible">
  <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
  <strong>Ups!</strong>&nbspLa opción `+ idt +` debe ser completada antes de añadir una nueva
</div>`).insertAfter("nav");
}
});
});
