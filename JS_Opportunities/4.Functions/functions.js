'use strict'

// 1
function getWarrantyCost(period = 0) {
	switch (period) {
		case 0:
			return 0;
		case 1:
			return 1250;
		case 2:
			return 2300;
	}
}

var warrantyCost = getWarrantyCost(2);
console.log(`Дополнительное гарантийное обслуживание: ${warrantyCost} Q`);


// 2
function getEtchingCost(sentence) {
	var wordsQuantity = sentence.split(' ').length;
	return wordsQuantity * 11;
}

var sentences = ['Красивая надпись', '', undefined];
var sentence = sentences[2];

var etchingCost = (sentence) ? getEtchingCost(sentence) : 0;
console.log(`\nПодарочная упаковка и гравировка: ${etchingCost} Q`);


// 3
var addresses = ['Луна', 'Крабовидная туманность',
	'Галактика Туманность Андромеды', 'Туманность Ориона',
	'Звезда смерти'];

function getDeliveryCost (isDeliveryNeed, deliveryAddress) {
	var isDeliveryAvailable = (addresses.includes(deliveryAddress)) ? true : false;

	if (!isDeliveryNeed) {
		return 0;
	} else if (!isDeliveryAvailable) {
		return NaN;
	} else if (isDeliveryNeed && isDeliveryAvailable) {
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
		}
		return deliveryCost;
	} else {
		console.log('Ошибка при расчете стоимости доставки');
	}
}

//var deliveryCost = getDeliveryCost(true, 'Луна');
//var deliveryCost = getDeliveryCost(true, 'Звезда смерти');
var deliveryCost = getDeliveryCost(false, undefined);
//var deliveryCost = getDeliveryCost(true, 'Юпитер');

if (deliveryCost === 0) {
	console.log('\nДоставка не требуется');
} else if (isNaN(deliveryCost) && deliveryCost !== 'договорная цена') {
	console.log('\nОшибка при расчете стоимости доставки');
} else {
	console.log(`\nСтоимость доставки: ${deliveryCost} Q`);
}


// 4
console.log('\n==============4==============');

function getOrderTotalReport(productsCost, warrantyPeriod, etchingString,
	isDeliveryNeed, deliveryAddress) {

	var addresses = ['Луна', 'Крабовидная туманность',
		'Галактика Туманность Андромеды', 'Туманность Ориона',
		'Звезда смерти'];

	function getWarrantyCost(period) {
		switch (period) {
		case 0:
			return 0;
		case 1:
			return 1250;
		case 2:
			return 2300;
		}
	}

	function getEtchingCost(sentence) {
		if (!sentence) {
			return 0;
		} else {
			var wordsQuantity = sentence.split(' ').length;
			return wordsQuantity * 11;
		}
	}

	function getDeliveryInfo(isDeliveryNeed, deliveryAddress) {
		var isDeliveryAvailable = addresses.includes(deliveryAddress) ? true : false;

		if (!isDeliveryNeed) {
			return ['Доставка не требуется.', 0];
		} else if (!isDeliveryAvailable) {
			return ['Ошибка при расчете стоимости доставки.', 0];
		} else if (isDeliveryNeed && isDeliveryAvailable) {
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
			}
			return [`Доставка в область ${deliveryAddress}: ${deliveryCost} Q.`, deliveryCost];
		} else {
			return ['Ошибка при расчете стоимости доставки.', 0];
		}
	}

	if (!warrantyPeriod) warrantyPeriod = 0;
	var warrantyCost = getWarrantyCost(warrantyPeriod);
	var etchingCost = getEtchingCost(etchingString);
	var [deliveryMessage, deliveryCost] = getDeliveryInfo(isDeliveryNeed, deliveryAddress);
	var nuance = (typeof(deliveryCost) === 'string') ? ' + ' : 0;
	var orderTotalCost = productsCost + warrantyCost + etchingCost + nuance + deliveryCost;

	console.log(`\nОбщая стоимость заказа: ${orderTotalCost} Q.`);
	console.log(`Из них ${warrantyCost} Q за гарантийное обслуживание на ${warrantyPeriod} год/года.`);
	console.log(`Гравировка на сумму ${etchingCost} Q.`);
	console.log(deliveryMessage);
}

getOrderTotalReport(5000, 2, 'Brotherhood of steel', true, 'Туманность Ориона');
getOrderTotalReport(7000, 0, '', false, undefined);
getOrderTotalReport(15000, undefined, 'From Earth with love', true, 'Сатурн');
getOrderTotalReport(500, 1, undefined, true, 'Звезда смерти');