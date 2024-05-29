/* global $ */

$(document).ready(function () {
  $('#add_item').click(function () {
    const newListItem = $('<li>Item</li>');
    $('ul.my_list').append(newListItem);
  });
});
