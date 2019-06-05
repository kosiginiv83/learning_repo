'use strict'

var positions = [
  {
    title: 'Телепорт бытовой VZHIH-101',
    price: 10000,
    discount: 7,
    available: 3
  },
  {
    title: 'Ховерборд Mattel 2016',
    price: 9200,
    discount: 4,
    available: 14
  },
  {
    title: 'Меч световой FORCE (синий луч)',
    price: 57000,
    discount: 0,
    available: 1
  }
];


// 1
const itemPrototype = {
  hold(amount = 1) {
    if (this.available < amount) {
      return false;
    }
    this.available -= amount;
    this.holded += amount;
    return true;
  },

  unhold(amount = this.holded) {
    if (this.holded < amount) {
      return false;
    }
    this.available += amount;
    this.holded -= amount;
    return true;
  },

  toString() {
    return `${this.title} (остаток ${this.available}, в резерве ${this.holded})`;
  }
};

function createItem(title, amount) {
  const item = Object.create(itemPrototype);
  item.title = title;
  item.available = amount;
  item.holded = 0;
  return item;
}

const items = [];
for (let item of positions) {
  items.push(createItem(item.title, item.available));
}

items[0].hold(2);
items[1].hold(8);
items[1].hold(12);
items[2].hold();

for (let item of items) {
  console.log(`Товар ${item}`);
}

console.log('\n===Отмена резерва===');
items[0].unhold();
items[1].unhold(12);
items[1].unhold(5);
items[2].unhold(1);

for (let item of items) {
  console.log(`Товар ${item}`);
}


console.log();
// 2
try {
  for (let item of positions) {
    //item.finalPrice;
    item.finalPriceValue = item.price * (1 - item.discount/100);
    item.priceValue = item.price;
    item.discountValue = item.discount;
  }

  const changePrice = {
    set(newPrice) {
      this.finalPriceValue = Math.round(newPrice * (1 - this.discountValue/100));
      this.priceValue = newPrice;
    },
    get() {
      return this.priceValue;
    }
  };

  const changeDiscount = {
    set(newDiscount) {
      this.finalPriceValue = Math.round(this.priceValue * (1 - newDiscount/100));
      this.discountValue = newDiscount;
    },
    get() {
      return this.discountValue;
    }
  };

  const changeFinalPrice = {
    set(newFinalPrice) {
      if (newFinalPrice > this.price) {
        throw [this.title, ' Цена со скидкой больше базовой цены'];
      }
      this.discountValue = Math.floor((1 - newFinalPrice/this.priceValue) * 100);
      this.finalPriceValue = newFinalPrice;
    },
    get() {
      return this.finalPriceValue;
    }
  };

  for (let item of positions) {
    Object.defineProperty(item, 'finalPrice', changeFinalPrice);
    Object.defineProperty(item, 'price', changePrice);
    Object.defineProperty(item, 'discount', changeDiscount);
  }

  positions[0].price = 15000;
  console.log(positions[0].title, 'price', positions[0].price);
  console.log(positions[0].title, 'finalPrice', positions[0].finalPrice);
  console.log(positions[0].title, 'discount', positions[0].discount);

  positions[1].discount = 50;
  console.log(positions[1].title, 'price', positions[1].price);
  console.log(positions[1].title, 'finalPrice', positions[1].finalPrice);
  console.log(positions[1].title, 'discount', positions[1].discount);

  positions[2].finalPrice = 40000;
  console.log(positions[2].title, 'price', positions[2].price);
  console.log(positions[2].title, 'finalPrice', positions[2].finalPrice);
  console.log(positions[2].title, 'discount', positions[2].discount);

  positions[2].finalPrice = 60000;

} catch(err) {
  console.log(`Ошибка: ${err}`);
}


console.log();
// 3
function isValidPosition(form, requiredFields) {
  let formKeys = Object.keys(form);
  let isIn = (item) => formKeys.includes(item);
  let isAllKeysExist = requiredFields.every(isIn);

  let formValues = Object.values(form);
  let isFilled = (item) => item !== '' && item !== undefined;
  let isAllValuesExist = formValues.every(isFilled);

  return (isAllKeysExist && isAllValuesExist) ? true : false;
}

const requiredFields = [ 'title', 'price', 'discount' ];
let form1 = {
  title: 'Товар Телепорт бытовой VZHIH-101',
  price: 7800,
  discount: 0
};
let form2 = {
  title: 'Товар Телепорт бытовой VZHIH-101',
  discount: 10
};
let form3 = {
  title: 'Товар Телепорт бытовой VZHIH-101',
  price: 7800,
  discount: undefined
};

if ( isValidPosition(form1, requiredFields) ) {
  console.log('Форма № 1 заполнена верно');
} else {
  console.log('В форме № 1 не заполнены необходимые поля');
}

if ( isValidPosition(form2, requiredFields) ) {
  console.log('Форма № 2 заполнена верно');
} else {
  console.log('В форме № 2 не заполнены необходимые поля');
}

if ( isValidPosition(form3, requiredFields) ) {
  console.log('Форма № 3 заполнена верно');
} else {
  console.log('В форме № 3 не заполнены необходимые поля');
}