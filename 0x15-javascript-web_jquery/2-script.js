const $headerElement = $('header');
const $redHeader = $('div#red_header');

$redHeader.on('click', function () {
	$headerElement.css('color', '#FF0000');
});
