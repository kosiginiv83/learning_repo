'use strict'

const clients = [{
  name: 'Филип Фрай',
  email: 'fray@mail.un',
  isSubscribed: false,
  orders: [ 11700, 1980, 450, 5500 ]
}, {
  name: 'Бендер Сгибатель Родригес',
  email: 'bender.rodriges@rambler.un',
  isSubscribed: true,
  orders: [ 440, 226, 7650, 2990, 70 ]
}, {
  name: 'Доктор Джон Зоидберг',
  email: 'zoidberg-md@list.un',
  isSubscribed: true,
  orders: [ 720 ]
}];


// 1
clients.findByName = name => {
  let foundElement = clients.find( item => item.name === name );
  return foundElement;
}

const clientOne = clients.findByName('Доктор Джон Зоидберг');
console.log(clientOne.email); // zoidberg-md@list.un

const clientTwo = clients.findByName('Люрр');
console.log(typeof clientTwo); // undefined

const clientThree = clients.findByName('Бендер Сгибатель Родригес');
console.log(clientThree.orders.length); // 5


console.log();
// 2
const compareByTotalSumm = (left, right) => {
  let sumTotal = client => client.orders.reduce( (memo, item) => {
    return memo + item;
  }, 0 );

  let sumLeft = sumTotal(left);
  let sumRight = sumTotal(right);

  if ( sumLeft < sumRight ) {
    return 1;
  } else if ( sumLeft > sumRight ) {
    return -1;
  } else {
    return 0;
  }
};

clients
  .sort(compareByTotalSumm)
  .forEach(client => console.log(client.name));
// Филип Фрай
// Бендер Сгибатель Родригес
// Доктор Джон Зоидберг


console.log();
// 3
function sendMail(email) {
  console.log(`Письмо отправлено на адрес ${email}`);
}

const getSubscribedEmails = list => {
  let subscribed = list
    .filter( item => item.isSubscribed === true )
    .map( item => item.email );
  return subscribed;
};

getSubscribedEmails(clients).forEach(sendMail);