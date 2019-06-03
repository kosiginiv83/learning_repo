'use strict'

var positions = [
  'Телепорт бытовой VZHIH-101',
  'Отвертка ультразвуковая WHO-D',
  'Ховерборд Mattel 2016',
  'Нейтрализатор FLASH black edition',
  'Меч световой FORCE (синий луч)'
];

var prices = [
  10000,
  4800,
  9200,
  2500,
  57000
];

var hitName = positions[2], hitPrice = prices[2];


// 1
var hit = {};
hit.name = hitName;
hit.price = hitPrice;
console.log(`Хит продаж мартобря: <${hit.name}> цена ${hit.price} Q`);


console.log();
// 2
var items = [];

for (let i = 0; i < positions.length; i++) {
	let item = {name: positions[i], price: prices[i]};
	items.push(item);
}

console.log(`Купите ${items[4].name} по цене ${items[4].price} Q`);


console.log();
// 3
var showDiscount = ({name, price}, quantity) => {
	let discount;

	if (quantity < 10) {
		discount = 0.05;
	} else if (quantity < 50) {
		discount = 0.07;
	} else if (quantity < 100) {
		discount = 0.10;
	} else {
		discount = 0.15;
	};

	let orderCost = price * quantity;
	let orderCostDiscount = Math.round(orderCost * (1 - discount));
	let benefit = orderCost - orderCostDiscount;

	console.log(`${name} — стоимость партии из ${quantity} штук ${orderCostDiscount} Q (скидка ${Math.round(discount * 100)} %), ваша выгода ${benefit} Q!`);
}

showDiscount(items[0], 12);
showDiscount(items[3], 97);


console.log();
// 4
items[3].amount = 4;

var updateAmount = (product, outgo = 1) => {
	var {name, amount} = product;

  if (typeof(amount) !== 'undefined') {
		if (amount === 0 || outgo > amount) {
			console.log(`${name} закончился на складе.`);
		} else if (outgo < amount) {
			product.amount -= outgo;
			console.log(`${name} — остаток ${product.amount} шт.`);
		} else if (outgo === amount) {
			product.amount -= outgo;
			console.log(`Это был последний ${name}, вам повезло!`);
		}
	} else {
		return;
	}
}

updateAmount(items[1], 17);
updateAmount(items[3], 3);
updateAmount(items[3]);
updateAmount(items[3]);