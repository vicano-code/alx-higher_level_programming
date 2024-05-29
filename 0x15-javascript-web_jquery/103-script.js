/* global $ */

$(document).ready(function () {
  function getTranslation () {
    const url = 'https://hellosalut.stefanbohacek.dev/';
    const langCode = $('#language_code').val();
    $.get(url, { lang: langCode }, function (response) {
      // Update response in html tag with id 'hello'
      $('#hello').text(response.hello);
    });
  }
  // Click event listener for thetranslate button
  $('#btn_translate').click(function () {
    getTranslation();
  });
  // Keypress event listener for ENTER key
  $('#language_code').keypress(function (event) {
    // Check if the key pressed is ENTER (key code 13)
    if (event.which === 13) {
      getTranslation();
    }
  });
});
