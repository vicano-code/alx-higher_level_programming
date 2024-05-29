/* global $ */

$(document).ready(function () {
  $('#add_item').click(function () {
    const newListItem = '<li>Item</li>';
    $('UL.my_list').append(newListItem);
  });
  $('#remove_item').click(function () {
    $('UL.my_list li:last').remove();
  });
  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
