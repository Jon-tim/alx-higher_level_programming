const $hello = $('div#hello');

$(document).ready(function() {
	$.ajax({
		url: 'https://hellosalut.stefanbohacek.dev/?lang=fr';
		method: 'GET';
		dataType: 'json';
		success: function(data) {
			const dataValue = data.hello;

			$hello.text(dataValue);
		};
	});
});
