const $ul = $('ul.my_list');
const addItem = $('div#add_item');

$addItem.on('click', function () {
	$ul.append('<li>Item</li>');
});
