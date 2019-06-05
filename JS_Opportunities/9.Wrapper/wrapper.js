'use strict'

function showSpecialPrice() {
  console.log('Введен секретный код. Все цены уменьшены вдвое!');
}


// 1
function fixAmount(amount) {
  if (isNaN(amount)) {
    amount = Number.parseFloat(amount.replace(',', '.'));
    return amount ? amount : -1;
  }
  return amount;
}

const orders = [
  { price: 21, amount: 4 },
  { price: 50, amount: '17 штук' },
  { price: 7, amount: '1,5 килограмма' },
  { price: 2, amount: ' 2.7 метра ' },
  { price: 1, amount: 'семь единиц' }
];

for (let order of orders) {
  let result = fixAmount(order.amount);
  console.log(`Заказ на сумму: ${result * order.price} Q`);
}


console.log();
// 2
var keyLog = new String();

function handleKey(char) {
  keyLog = keyLog.concat(char.toLowerCase());
  if (keyLog.slice(-4) === 'r2d2') {
    showSpecialPrice();
  }
}

var keys = ['2', '4', 'R', '2', 'd', '2'];
for (let key of keys) {
  handleKey(key);
}


console.log();
// 3
function parseData(keys, data, separator = ',') {
  let itemList = [];

  for (let item of data) {
    item = item.split(separator);
    item = item.map((value) => {
      return value.trim();
    });

    let itemObj = {};
    for (let i = 0; i < keys.length; i++) {
      itemObj[keys[i]] = item[i];
    }

    itemList.push(itemObj);
  }

  return itemList;
}

let data = [
  '12,Телепорт бытовой VZHIH-101 ,17,10000',
  '77, Меч световой FORCE (синий луч), 2,57000'
];
let items = parseData(['id', 'name', 'amount', 'price'], data);
console.log(items);

console.log();
data = [
  '12;Телепорт бытовой VZHIH-101 ;17;10000',
  '77; Меч световой FORCE (синий луч); 2;57000'
];
items = parseData(['id', 'name', 'amount', 'price'], data, ';');
console.log(items);