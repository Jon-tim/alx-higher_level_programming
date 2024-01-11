$(document).ready(function () {

	$('input#btn_translate').on('click', function () {
		const languageCode = $('input#language_code').val();

		$.ajax({
			url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
			method: 'GET',
			success: function (data) {
				$('div#hello').text(data.hello);
			},
		});
	});
});

