$(document).ready(function() {
  console.log('This is hello from github');
  var status_select = '<select style="width: 130px;">' +
      '<option value="1">Pending</option>' +
      '<option value="2">Processing</option>' +
      '<option value="2">Cancelled</option>' +
    '</select>'
  $('.field-status').each(function(){
    $(this).html(status_select);
  })
});
