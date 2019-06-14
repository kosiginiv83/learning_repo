'use strict'

function rand(min, max) {
  return Math.ceil((max - min + 1) * Math.random()) + min - 1;
}

function generateId() {
  return Array(4).fill(1).map(value => rand(1000, 9999)).join('-');
}

const pointsInfo = [
  { title: 'Темная сторона Луны', coords: [500, 200, 97] },
  { title: 'Седьмое кольцо Юпитера', coords: [934, -491, 712] },
  { title: 'Саратов', coords: [30, 91, 77] }
];


// 1
function OrdersTeleportationPoint(title, x, y, z) {
  this.title = title;
  this.x = x;
  this.y = y;
  this.z = z;
  this.getDistance = (x, y, z) => {
    return Math.sqrt( Math.pow(this.x - x, 2) + Math.pow(this.y - y, 2) + Math.pow(this.z - z, 2) );
  };
}

const point = new OrdersTeleportationPoint(pointsInfo[0]['title'], ...pointsInfo[0]['coords']);
let distance = point.getDistance(100, -100, 33);
console.log(`Расстояние до пункта «${point.title}» составит ${distance.toFixed(0)} единиц`);

const point2 = new OrdersTeleportationPoint(pointsInfo[1]['title'], ...pointsInfo[1]['coords']);
distance = point2.getDistance(500, 100, -133);
console.log(`Расстояние до пункта «${point2.title}» составит ${distance.toFixed(0)} единиц`);

const point3 = new OrdersTeleportationPoint(pointsInfo[2]['title'], ...pointsInfo[2]['coords']);
distance = point3.getDistance(-200, 100, 33);
console.log(`Расстояние до пункта «${point3.title}» составит ${distance.toFixed(0)} единиц`);


console.log();
// 2
function OrdersTeleportationPointLocator(points) {
  try {
    if ( !Array.isArray(points) ) throw 'Передан не массив';
    this.points = [];

    for (let point of points) {
      if ( !OrdersTeleportationPoint.prototype.isPrototypeOf(point) ) continue;
      this.points.push(point);
    }

  } catch(err) {
    console.log(err);
  }
}

OrdersTeleportationPointLocator.prototype.getClosest = function(x, y, z) {
  let distances = [];

  for (let point of this.points) {
    distance = point.getDistance(x, y, z);
    distances.push(distance);
  }

  return this.points[ distances.indexOf(Math.min.apply(null, distances)) ];
};

const points = pointsInfo.map(point => new OrdersTeleportationPoint(point.title, ...point.coords));
const locator = new OrdersTeleportationPointLocator(points);

var closestPoint = locator.getClosest(333, 294, 77);
console.log(`Ближайший пункт телепортации заказов «${closestPoint.title}»`);

closestPoint = locator.getClosest(30, 30, 30);
console.log(`Ближайший пункт телепортации заказов «${closestPoint.title}»`);

closestPoint = locator.getClosest(900, -300, 700);
console.log(`Ближайший пункт телепортации заказов «${closestPoint.title}»`);


console.log();
// 3
function LoyaltyCard(name, sum) {
  this.owner = name;
  this.discountValue = 0;
  this.orders = [sum];

  Object.defineProperties(this, {
    discount: {
      get: () => {
        if (this.balance <= 3000) {
          this.discountValue = 0;
        } else if (this.balance <= 5000) {
          this.discountValue = 3;
        } else if (this.balance <= 10000) {
          this.discountValue = 5;
        } else {
          this.discountValue = 7;
        }

        return this.discountValue;
      }
    },

    balance: {
      get: () => {
        let result = this.orders.reduce( (sum, item) => {
          return sum + item;
        }, 0);

        return result;
      }
    },

    id: {
      get: () => {
        if (!this.idValue) {
          this.idValue = generateId();
        }

        return this.idValue;
      }
    }
  });
}


LoyaltyCard.prototype = {
  getFinalSum(sum) {
    return sum * ( 1 - this.discount / 100 );
  },

  append(order) {
    this.orders.push(order);
  },

  show() {
    console.log(
    `\nКарта ${this.id}:
    Владелец: ${this.owner}
    Баланс: ${this.balance} Q
    Текущая скидка: ${this.discount} %
    Заказы:`
    );

    for ( let order of this.orders.entries() ) {
      console.log(`\t#${order[0] + 1} на сумму ${order[1]} Q`);
    }
  }
};


const card = new LoyaltyCard('Иванов Иван', 6300);

let newOrderSum = 7000;
let finalSum = card.getFinalSum(newOrderSum);
console.log(`Итоговая сумма для заказа на ${newOrderSum} Q по карте
  составит ${finalSum} Q. Скидка ${card.discount} %.`);

card.append(newOrderSum);
console.log(`Баланс карты после покупки ${card.balance} Q.`);
card.show();


console.log();
newOrderSum = 12000;
finalSum = card.getFinalSum(newOrderSum);
console.log(`Итоговая сумма для заказа на ${newOrderSum} Q по карте
  составит ${finalSum} Q. Скидка ${card.discount} %.`);

card.append(newOrderSum);
console.log(`Баланс карты после покупки ${card.balance} Q.`);
card.show();


// Проверка того, что нельзя напрямую изменить данные карты
console.log();
//card.discount = 0.5;
//card.id = 111;
//card.balance = 50000;