$(function () {
  $("#datetimepicker1").datetimepicker({
    defaultDate: new Date(),
    format: 'DD/MM/YY',
    usecurrent: 'true',  
  });
});

$('.add_option').click(function(){
var idt = parseInt($('#tablaOpciones tr:last').attr('id')) + 1;
var option = idt+1;
console.log(idt);
console.log("holi");
var lastMain = $('#id_form-'+(idt-1)+'-maindish').val();
console.log(lastMain);
if (lastMain != "") {
  $('#tablaOpciones tr:last').after(`
  <tr id="`+idt+`">
<td style="text-align: center">
    ` + option + `
</td>
<td>
    <input type="text" name="form-`+idt+`-maindish" id="id_form-`+idt+`-maindish" class="form-control">
</td>
<td style="text-align: center">
    <input type="checkbox" name="form-`+idt+`-salad" id="id_form-`+idt+`-salad">
</td>
<td style="text-align: center">
    <input type="checkbox" name="form-`+idt+`-dessert" id="id_form-`+idt+`-dessert">
</td>
</tr>
  `);}
});
