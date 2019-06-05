'use strict'

var positions = [
  {
    title: 'Телепорт бытовой VZHIH-101',
    producer: {
      name: 'Рязанский телепортостроительный завод',
      deferPeriod: 10,
      lot: 3
    },
    price: 10000
  },
  {
    title: 'Ховерборд Mattel 2016',
    producer: {
      name: 'Волжский Ховерборд Завод',
      deferPeriod: 24,
      lot: 14
    },
    price: 9200
  },
  {
    title: 'Меч световой FORCE (синий луч)',
    producer: {
      name: 'Тульский оружейный комбинат',
      deferPeriod: 5,
      lot: 1
    },
    price: 57000
  }
];


// 1
var lotCalculator = ({title, price, producer}, amount) => {
  let lot = producer.lot;
  let lots = Math.ceil(amount / lot);
  let total = lot * lots * price;
  return {lots: lots, total: total};

  // Я бы добавил в объект больше свойств для вывода
  //return {lots: lots, total: total, title: title, amount: amount};
}

let amount = 15;
let result1 = lotCalculator(positions[1], amount);
//console.log(result1); // { lots: 2, total: 257600 }
console.log(`${positions[1].title} ${amount} штук: заказать партий ${result1.lots}, стоимость ${result1.total} Q`);

amount = 1;
let result2 = lotCalculator(positions[2], amount);
//console.log(result2); // { lots: 1, total: 57000 }
console.log(`${positions[2].title} ${amount} штук: заказать партий ${result2.lots}, стоимость ${result2.total} Q`);

amount = 3;
let result3 = lotCalculator(positions[0], amount);
//console.log(result3); // { lots: 1, total: 30000 }
console.log(`${positions[0].title} ${amount} штук: заказать партий ${result3.lots}, стоимость ${result3.total} Q`);


console.log();
// 2
const deferedPayments = [];

var deferPay = (producer, sum, purchaseDate) => {
  const paymentDate = new Date(purchaseDate);
  paymentDate.setDate(paymentDate.getDate() + producer.deferPeriod);

  deferedPayments.push({
    producer: producer,
    paymentDate: paymentDate,
    amount: sum
  });
};

deferPay(positions[0].producer, 15000, new Date(2030, 1 - 1, 15));
deferPay(positions[1].producer, 11000, new Date(2030, 2 - 1, 12));
deferPay(positions[2].producer, 38000, new Date(2030, 3 - 1, 22));

for (let item of deferedPayments) {
  console.log(`${item.paymentDate.toLocaleDateString('ru-Ru')}: ${item.producer.name}, сумма ${item.amount} Q`);
}

console.log('\n', deferedPayments.length);
console.log(deferedPayments[0].producer.name);
console.log(deferedPayments[0].amount);
console.log(deferedPayments[0].paymentDate);


console.log();
// 3

function loadCurrencyJSON() {
  return '{"AUD":44.95,"AZN":33.73,"GBP":73.42,"AMD":0.12,"BYN":30.96,"BGN":32.01,"BRL":18.8,"HUF":0.2,"DKK":8.42,"USD":58.85,"EUR":62.68,"INR":0.88,"KZT":0.18,"CAD":44.74,"KGS":0.85,"CNY":8.55,"MDL":2.94,"NOK":7.02,"PLN":14.55,"RON":13.92,"ZZZ":79.91,"SGD":41.36,"TJS":7.43,"TRY":15.97,"TMT":16.84,"UZS":0.02,"UAH":2.16,"CZK":2.32,"SEK":6.6,"CHF":58.69,"ZAR":4.4,"KRW":0.05,"JPY":0.52}';
}

var convertCurrency = (amount, from, to) => {
  try {
    let currencies = loadCurrencyJSON();
    currencies = JSON.parse(currencies);
    let sum = +(amount * currencies[from] / currencies[to]).toFixed(2);
    return sum;
  } catch(err) {
    console.log(err);
  }
}

let price1 = convertCurrency(7000, 'ZZZ', 'USD');
console.log(`Сумма ${price1} USD`);
// Сумма 9505.01 USD

let price2 = convertCurrency(790, 'EUR', 'ZZZ');
console.log(`Сумма ${price2} ZZZ`);
// Сумма 619.66 ZZZ

let price3 = convertCurrency(50000, 'CZK', 'JPY');
console.log(`Сумма ${price3} JPY`);
// Сумма 223076.92 JPY
console.log(typeof price3);