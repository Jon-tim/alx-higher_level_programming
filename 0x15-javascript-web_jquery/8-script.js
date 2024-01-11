const $ul = $('ul#list_movies');

$.ajax({
	url: 'https://swapi-api.alx-tools.com/api/films/?format=json';
	method: 'GET';
	dataType: 'json';
	success: function(data) {
		const moviesList = data.results;

		$.each(moviesList, function(index, movie) {
			$ul.append('<li>' + movie.title + '</li>');
		});
	};
});
