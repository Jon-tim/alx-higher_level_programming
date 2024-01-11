const $headerElement = $('header');
const $toggleHeader = $('div#toggle_header');

$toggleHeader.on('click', function () {
	const currentClass = $headerElement.attr('class');

	if (currentClass === 'green') {
		$headerElement.toggleClass(`${currentClass} red`);
	}

	if (currentClass === 'red') {
		$headerElement.toggleClass(`${currentClass} green`);
	}
});
