// 1
'use strict'
var productName;
var productPrice;

// 2
productName = 'Телепорт бытовой VZHIH-101';
productPrice = 10000;
console.log(`В наличии имеется: «${productName}»`);
console.log(`Стоимость товара ${productPrice} Q`);

// 3
var goodsAmount = 2;
var discount = 0.1;
var total = (productPrice * (1-discount)) * goodsAmount;
console.log(`Цена покупки составит ${total} Q`);

// 4
var accountTotal = 52334224;
var teleportPurchasePrice = 6500;
var teleportAmount = Math.floor(accountTotal / teleportPurchasePrice);
var accountRest = accountTotal % teleportPurchasePrice;
console.log(`Мы можем закупить ${teleportAmount} единиц товара, после закупки на счету останется ${accountRest} Q`);