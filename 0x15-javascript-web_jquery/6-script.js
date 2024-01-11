const $headerElement = $('header');
const $updateHeader = $('div#update_header');

$updateHeader.on('click', function () {
	$headerElement.text('New Header!!!');
});
