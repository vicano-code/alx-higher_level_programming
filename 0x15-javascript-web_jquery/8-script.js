/* global $ */

$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data) {
    const titleList = [];
    for (let i = 0; i < data.results.length; i++) {
      titleList[i] = data.results[i].title;
      const newListItem = '<li></li>';
      $('#list_movies').append(newListItem);
    }
    $('#list_movies li').each(function (index) {
      $(this).append(titleList[index]);
    });
  });
});
