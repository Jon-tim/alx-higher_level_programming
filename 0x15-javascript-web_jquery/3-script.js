const $headerElement = $('header');
const $redClass = $('div#red_header');

$redClass.on('click', function () {
	$headerElement.addClass('red');
});
