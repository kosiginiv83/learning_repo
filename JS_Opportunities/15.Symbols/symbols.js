'use strict'

// 1
class BarcodeGenerator {
  constructor(size = 1) {
    this.size = size;
    const prefix = Symbol();
  }

  get prefix() {
    return prefix;
  }

  create() {
    let multiplier = Math.pow(10, this.size - 1);
    let barcode = Math.round( (Math.random() * 9 + 1) * multiplier );

    let result = (this[BarcodeGenerator.prefix] !== undefined) ?
      `${this[BarcodeGenerator.prefix]}-${barcode}` :
      `${barcode}`;

    return result;
  }
}


const generator = new BarcodeGenerator(4);

generator[BarcodeGenerator.prefix] = 'AA';
console.log(generator.create());

generator[BarcodeGenerator.prefix] = 'XX';
console.log(generator.create());
console.log(generator.create());
console.log(generator.create());

delete generator[BarcodeGenerator.prefix];
console.log(generator.create());


console.log();
// 2
class HexRange {
    constructor(from, to) {
        range = [...Array.from( Array(to - from + 1).keys(), k => k + from )];
        this.range16 = range.map( item => item.toString(16) );
    }

    [Symbol.iterator]() {
        return this.range16[Symbol.iterator]();
    }
}

let queue = new HexRange(247, 253);
console.log(...queue);

queue = new HexRange(2400718, 2400722);
for (let item of queue) {
  console.log(item);
}


console.log();
// 3
class DateRange {
  constructor(from, to) {
    let workRange = [];
    let daysAmount = Math.floor( (to.getTime() - from.getTime()) / (1000 * 60 * 60 * 24) ) + 1;
    let toDate = to.getDate();
    let date = new Date(from);

    for (let i = 0; i <= daysAmount; i++) {
      let isWorkDay = ![0, 6].includes(date.getDay());
      if (isWorkDay) {
        workRange.push(new Date(date));
      }
      date.setDate(date.getDate() + 1);
    }

    this.workRange = workRange;
  }

  [Symbol.iterator]() {
      return this.workRange[Symbol.iterator]()
  }
}


const from = new Date(2019, 5, 10, 23, 59);
const to = new Date(2019, 5, 17, 0, 1);
let range = new DateRange(from, to);

for (let day of range) {
  console.log(day.toLocaleDateString('ru-Ru'));
}