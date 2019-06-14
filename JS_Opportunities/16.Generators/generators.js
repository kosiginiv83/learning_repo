'use strict'


function hslToRgb(h, s, l) {
  let r, g, b;

  if(s == 0) {
    r = g = b = l; // achromatic
  } else {
    const hue2rgb = function (p, q, t) {
      if(t < 0) t += 1;
      if(t > 1) t -= 1;
      if(t < 1/6) return p + (q - p) * 6 * t;
      if(t < 1/2) return q;
      if(t < 2/3) return p + (q - p) * (2/3 - t) * 6;
      return p;
    };

    const q = l < 0.5 ? l * (1 + s) : l + s - l * s;
    const p = 2 * l - q;
    r = hue2rgb(p, q, h + 1/3);
    g = hue2rgb(p, q, h);
    b = hue2rgb(p, q, h - 1/3);
  }

  function colorToHex(color) {
    let hex = Math.round(color * 255).toString(16);
    return hex.length < 2 ? `0${hex}` : hex;
  }

  const color = [r, g, b].map(colorToHex).join('');
  return `#${color}`;
}


class Order {
  constructor(id, weight) {
    this.id = id;
    this.weight = weight;
  }
}

class Truck extends Array {
  constructor(number, weightLimit) {
    super();
    this.number = number;
    this.weightLimit = weightLimit;
  }

  add(order) {
    if (!this.isFit(order)) {
      return false;
    }
    this.push(order);
    return true;
  }

  isFit(order) {
    return this.weightLimit >= (this.totalWeight + order.weight);
  }

  get totalWeight() {
    return this.reduce((total, order) => total + order.weight, 0);
  }

  show() {
    console.log(`Машина №${this.number} (общий вес груза ${this.totalWeight}кг):`);
    this.forEach(order => console.log(`\tЗаказ #${order.id} ${order.weight}кг`));
  }
}


// 1
function* palette(amount) {
  let random = (min, max) => {
    return Math.random() * (max - min) + min;
  }

  let step = 360 / amount;
  let h, s, l;
  l = random(0, 1);
  s = random(0, 1);

  for (let i = 0; i < amount; i++) {
    h = random(0, step) / 360;
    yield hslToRgb(h, s, l);

    h += step;
  }
}

for (const color of palette(3)) {
  console.log(color);
}


console.log();
// 2
function* numberQuiz(number) {
  let result = yield 'Назовите число:';

  while (true) {
    if (result === number) {
      return `Вы угадали, это ${number}`;
    } else if (number > result) {
      result = yield `Больше, чем ${result}!`;
    } else if (number < result) {
      result = yield `Меньше, чем ${result}!`;
    }
  }
}

const attempts = [7, 4, 6, 5];
const quiz = numberQuiz(5);
let attempt, result;
do {
  result = quiz.next(attempt);
  console.log(result.value);
  attempt = attempts.shift();
} while (!result.done);


console.log();
// 3
class TruckPlanner {
  constructor(weightLimit) {
    this.weightLimit = weightLimit;
    this.trucksList = [];
  }

  add(order) {
    let trucksAmount = this.trucksList.length;
    let currentTruck = this.trucksList[trucksAmount - 1];

    if ( trucksAmount === 0 || !Truck.prototype.isFit.call(currentTruck, order) ) {
      this.trucksList.push( new Truck(trucksAmount + 1, this.weightLimit) );
      this.trucksList[trucksAmount].add(order);
    } else {
      currentTruck.add(order);
    }
  }
}

TruckPlanner.prototype[Symbol.iterator] = function* () {
  for (let truck of this.trucksList) {
    yield truck;
  }
}


const planner = new TruckPlanner(10);
planner.add(new Order(1, 2));
planner.add(new Order(2, 5));
planner.add(new Order(3, 4));
planner.add(new Order(4, 4));
planner.add(new Order(5, 1));
planner.add(new Order(6, 2));

for (const truck of planner) {
  truck.show();
}


/*
Машина №1 (общий вес груза 7кг):
  Заказ #1 2кг
  Заказ #2 5кг
Машина №2 (общий вес груза 9кг):
  Заказ #3 4кг
  Заказ #4 4кг
  Заказ #5 1кг
Машина №3 (общий вес груза 2кг):
  Заказ #6 2кг
*/