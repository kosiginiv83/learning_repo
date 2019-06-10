'use strict'

// 1
const checkCoupon = code => {
  code = code.replace(/[.,’\[\]\s]/g, '').toLowerCase();
  let codeLen = code.length;
  const left = () => code.slice(0, codeLen / 2);
  const right = () => code.slice( -(codeLen / 2) );
  const rightRev = str => (str === '') ? '' : rightRev(str.substr(1)) + str[0];

  return ( codeLen >= 10 && left() === rightRev(right()) ) ? true : false;
};

let codes = [
  'Madam, I’m Adam',
  'A man, a plan, a canal. Panama',
  '----<-------Eve------->-----',
  '[__777-x-44-x-777__]',
  '1234564321',
  'Olson in Oslo'
];

for (let code of codes) {
  let result = checkCoupon(code) ? 'подходит' : 'не подходит';
  console.log(`Код «${code}» ${result}`);
}


console.log();
// 2
const stripTags = text => {
  return text.replace(/<.[^<>\d]*>/g, '');
};

const texts = [
  '<strong>Наши</strong> <em>ховерборды</em> лучшие в <u>мире</u>!',
  '<EM>Световой меч</EM> в <strong>каждый</strong> дом!',
  '<p>Джедай без меча <em><strong>подобен джедаю с мечом</strong></em>, только без меча.</p>',
  '2 < 4 5 > 3'
];

for (let text of texts) {
  console.log(stripTags(text));
}


console.log();
// 3
const validate = (form, fields) => {
  return fields.every( field => field['rule'].test(form[field.name]) );
};

const fields = [
  { name: 'name', rule: /^[a-z ]{5,}$/i },
  { name: 'email', rule: /^[a-z]{3,}@[a-z]{3,}\.[a-z]{2,3}$/ },
  { name: 'phone', rule: /^\+7\d{10}$/ }
];

const forms = [
  { name: 'Ivan Ivanov', email: 'ivan@test.co', phone: '+79212753690' },
  { name: 'III', email: 'ivan@test', phone: '11111' },
  { name: 'Petr Petrov', email: 'petr@test.co', phone: '89642753111' },
  { name: 'Petr Petrov', email: 'petr@test.co' }
];

for (let form of forms) {
  console.log(form);
  if (validate(form, fields)) {
    console.log('Ошибок нет');
  } else {
    console.log('Форма заполнена неверно');
  }
}