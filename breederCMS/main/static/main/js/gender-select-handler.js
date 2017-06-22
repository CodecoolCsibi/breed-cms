$(document).ready(function () {
    $('.selectpicker').on('change', function(){
    var selected = $(this).find("option:selected").val();
    alert(selected);
    window.location.href = '../animal/' + selected
  });
});
