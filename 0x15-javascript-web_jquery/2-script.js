/* global $ */

// on click, updates the text color of the <header> element to red with JQuery
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
