document.addEventListener('DOMContentLoaded', function () {
	const $addItem = $('div#add_item');
	const $removeItem = $('div#remove_item');
	const $clearItems = $('div#clear_list');
	const $ul_list = $('ul.my_list');

	$addItem.on('click', function () {
		$ul_list.append('<li>' + 'item' + '</li>');
	});

	$removeItem.on('click', function () {
		$ul_list.find('li:last').remove();
	});

	$clearItems.on('click', function () {
		$ul_list.empty();
	});
});
