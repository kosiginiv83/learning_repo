'use strict'

const items = [
  {
    title: 'Телепорт бытовой VZHIH-101',
    available: 7,
    holded: 0
  },
  {
    title: 'Ховерборд Mattel 2016',
    available: 4,
    holded: 5
  },
  {
    title: 'Меч световой FORCE (синий луч)',
    available: 1,
    holded: 1
  }
];


// 1
try {
  const itemPrototype = {
    sell(field, amount = 1) {
      if (this[field] < amount) {
        throw `Недостаточно товара для продажи (${this[field]} из ${amount})`
      }
      this[field] -= amount;
      return true;
    },
    sellHolded(amount = 1) {
      return itemPrototype.sell.call(this, 'holded', amount);
    },
    sellAvailable(amount = 1) {
      return itemPrototype.sell.call(this, 'available', amount);
    }
  };

  var sellItem = (item, amount, isHolded = false) => {
    if (isHolded) {
      itemPrototype.sellHolded.call(item, amount);
    } else {
      itemPrototype.sellAvailable.call(item, amount);
    };
  };

  sellItem(items[2], 1);
  console.log(items[2].available); // 0
  console.log(items[2].holded); // 1

  sellItem(items[1], 4, true);
  console.log(items[1].available); // 4
  console.log(items[1].holded); // 1

  let item = { available: 0, holded: 1 };
  sellItem(item, 1, true);
  console.log(item.available); // 0
  console.log(item.holded); // 0

  item = { available: 3, holded: 2 };
  sellItem(item, 2);
  console.log(item.available); // 1
  console.log(item.holded); // 2

  sellItem(items[1], 2, true);

} catch (err) {
  console.log(err);
}


console.log();
// 2
function formatFull() {
  return `${this.title}:\n\tдоступно ${this.available} шт.\n\tв резерве ${this.holded} шт.`;
}

function formatLite() {
  return `${this.title} (${this.available} + ${this.holded})`;
}

function formatTotal() {
  return `${this.title} (Всего: ${this.available + this.holded})`;
}

function show(format) {
  console.log(format.call(this));
}

var showItems = (list, formatter) => {
  for (let item of list) {
    show.call(item, formatter);
  }
};

showItems(items, formatFull);
console.log('---');
showItems(items, formatLite);

const items2 = [
  {
    title: 'Отвертка ультразвуковая WHO-D',
    available: 17,
    holded: 10
  },
  {
    title: 'Нейтрализатор FLASH black edition',
    available: 24,
    holded: 15
  }
];

console.log('---');
showItems(items2, formatTotal);


console.log();
// 3
function createButton(title, onclick) {
  return {
    title,
    onclick() {
      console.log(`${title} ${onclick}`);
    },
    click() {
      this.onclick.call(this);
    }
  };
}

var createBuyButtons = (items) => {
  let buttonArr = [];
  for (let item of items) {
    var button = createButton.call(item, item.title, 'добавлен в корзину');
    buttonArr.push(button);
  }
  return buttonArr;
};

const buttons = createBuyButtons(items);
buttons[0].click();
buttons[2].click();
buttons[1].click();


console.log('---');
var createDelButtons = (items) => {
  let buttonArr = [];
  for (let item of items) {
    var button = createButton.call(item, item.title, 'удален из корзины');
    buttonArr.push(button);
  }
  return buttonArr;
};

const buttons2 = createDelButtons(items);
buttons2[0].click();
buttons2[2].click();
buttons2[1].click();