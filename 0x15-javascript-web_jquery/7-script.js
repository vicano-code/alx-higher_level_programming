/* global $ */

$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  // AJAX request to the API
  $.get(url, function (data) {
    const characterName = data.name;
    $('#character').text(characterName);
  });
});
