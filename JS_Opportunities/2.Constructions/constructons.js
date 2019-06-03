// 1
'use strict'

var productQuantityStore = 20;
var productQuantityOrder = 20;

if (productQuantityOrder > productQuantityStore) {
	console.log('На складе нет такого количества товаров')
} else if (productQuantityOrder === productQuantityStore) {
	console.log('Вы забираете весь товар c нашего склада!')
} else {
	console.log('Заказ оформлен')
}

// 2
var addresses = ['Луна', 'Крабовидная туманность',
	'Галактика Туманность Андромеды', 'Туманность Ориона',
	'Звезда смерти', 'другое'];
var deliveryAddress = addresses[1];

var deliveryCost;
var isDeliveryAvailable = true;

switch (deliveryAddress) {
	case 'Луна':
		deliveryCost = 150;
	break;
	case 'Крабовидная туманность':
		deliveryCost = 250;
	break;
	case 'Галактика Туманность Андромеды':
		deliveryCost = 550;
	break;
	case 'Туманность Ориона':
		deliveryCost = 600;
	break;
	case 'Звезда смерти':
		deliveryCost = 'договорная цена';
	break;
	default:
		isDeliveryAvailable = false;
		console.log('В ваш квадрант доставка не осуществляется');
}
if (isDeliveryAvailable) {
	console.log(`Стоимость доставки для области ${deliveryAddress}: ${deliveryCost} Q`);
}

// 3
try {
	var productPrice = 'ten';
	if (typeof(productPrice) !== 'number') {
		throw productPrice;
	} else {
		console.log('Цена товара введена корректно');
	}
} catch(err) {
	console.log(`Вы допустили ошибку: ${err} не является числом`);
}

// 4
var planets = ['Земля', 'Юпитер', 'Меркурий'];
var customerPlanet = planets[0];

var ages = [17, 18, 119, 120];
var customerAge = ages[1];

if (customerPlanet === 'Земля') {
	if (customerAge < 18) {
		console.log('Вы не достигли совершеннолетия');
	} else {
		console.log('Приятных покупок');
	}
} else if (customerPlanet === 'Юпитер') {
	if (customerAge < 120) {
		console.log('Сожалеем. Вернитесь на 120-й день рождения!');
	} else {
		console.log('Чистого неба и удачных покупок!');
	}
} else {
	console.log('Спасибо, что пользуетесь услугами нашего магазина!');
}