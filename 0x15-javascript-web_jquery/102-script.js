/* global $ */

$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/';
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    $.get(url, { lang: langCode }, function (response) {
      // Update response in html tag with id 'hello'
      $('#hello').text(response.hello);
    });
  });
});
