$(document).ready(function() {
  console.log('This is hello from github');
  var order_status = ['Processing','Ready to Pick','Inbound QC','Packing','Ready To Ship',
    'Shipped','Delivered','Closed','Cancelled','Return Requested','Return Denied',
    'Return accepted','Exchange','Refund'];
  var status_select = '<select data-selected_status="" style="width: 130px;">';
  $.each(order_status, function(i, v){
    status_select += '<option value="'+ v +'">'+ v +'</option>';
  });
  status_select += '</select>';
  $('.field-status').each(function(){
    var cur_status = $(this).html();
    $(status_select).data('selected_status', cur_status);
    $(this).html($(status_select));
  });
  
  
});
