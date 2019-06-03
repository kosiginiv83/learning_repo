'use strict'

var positions = [
  'Отвертка ультразвуковая WHO-D',
  'Ховерборд Mattel 2016',
  'Нейтрализатор FLASH black edition',
  'Меч световой FORCE (синий луч)',
  'Машина времени DeLorean',
  'Репликатор домашний STAR-94',
  'Лингвенсор 000-17',
  'Целеуказатель электронный WAY-Y'
];

// 1
var positionsQuantity = positions.length;
console.log('Список наименований');
for (let elem = 0; elem < positionsQuantity; elem++) {
	console.log(elem + 1, positions[elem]);
}

// 2
positions.push('Экзоскелет Trooper-111', 'Нейроинтерфейс игровой SEGUN', 'Семена дерева Эйва');
positionsQuantity = positions.length;
console.log('\nОкончательный список наименований');
for (let elem = 0; elem < positionsQuantity; elem++) {
	console.log(elem + 1, positions[elem]);
}

// 3
var indexNeedFirst = positions.indexOf('Машина времени DeLorean');
var deLorean = positions.splice(indexNeedFirst, 1);
positions.unshift(...deLorean);
var firstThreeProducts = positions.splice(0, 3);
console.log('\nПринять в первую очередь');
for (let i = 0; i < 3; i++) {
	console.log(i + 1, firstThreeProducts[i]);
}

// 4
var [first, second, third, fourth, fifth, ...another] = positions;
var firstFiveProducts = [];
firstFiveProducts.push(first, second, third, fourth, fifth);
console.log('\nВ магазине');
for (let elem of firstFiveProducts) {
	console.log(elem);
}
console.log('\nОстальные товары');
for (let elem of another) {
	console.log(elem);
}