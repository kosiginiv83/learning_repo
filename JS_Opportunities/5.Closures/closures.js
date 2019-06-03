'use strict'

// 1
function showTaxValue() {
	var taxVal = 0;
	return function (proceeds) {
		taxVal += proceeds * 0.73;
		console.log(`Налог с продаж (73 %), к оплате: ${taxVal} Q`);
	};
}

var taxValue = showTaxValue();
taxValue(1000);
taxValue(1000);
taxValue(1000);

console.log();


// 2
function showPackInfo() {
	var paperRest = 30;

	return function (x, y, z) {
		function yes() {
			paperRest -= square;
			console.log(`Заказ (${x}/${y}/${z} м) упакован, осталось упаковочной бумаги ${paperRest} м2`);
		}

		function no() {
			console.log(`Заказ (${x}/${y}/${z} м) не упакован, осталось упаковочной бумаги ${paperRest} м2`);
		}

		let square = Math.ceil(2 * (x*y + x*z + y*z));
		let result = (square <= paperRest) ? yes() : no();
	};
}

var packInfo = showPackInfo();
packInfo(1, 0.2, 0.7);
packInfo(100, 30, 7);
packInfo(2, 1, 1.5);
packInfo(20, 10, 10);
packInfo(0.5, 1.3, 2.1);


console.log('\n 3.v1');
// 3.v1
var teleportCharge = [7, 2, 1, 4, 8];
var updateCharge = [];

for (let i = 0; i < teleportCharge.length; i++) {
	updateCharge[i] = function () {
		if (teleportCharge[i] === 0) {
			console.log(`Телепорт ${i+1} недоступен, перезаряжается`);
		} else if (teleportCharge[i] === 1) {
			teleportCharge[i]--;
			console.log(`Телепорт ${i+1} использован, заряд — 0 единиц, требуется перезарядка!`);
		} else {
			teleportCharge[i]--;
			console.log(`Телепорт ${i+1} использован, заряд — ${teleportCharge[i]} единиц`);
		}
	};
}

updateCharge[0]();
updateCharge[0]();
updateCharge[1]();
updateCharge[1]();
updateCharge[2]();
updateCharge[2]();


console.log('\n 3.v2');
// 3.v2
function chargeUpdater() {
	var teleportCharge = [7, 2, 1, 4, 8];
	var updateCharge = [];

	for (let i = 0; i < teleportCharge.length; i++) {
		updateCharge[i] = function () {
			if (teleportCharge[i] === 0) {
				console.log(`Телепорт ${i+1} недоступен, перезаряжается`);
			} else if (teleportCharge[i] === 1) {
				teleportCharge[i]--;
				console.log(`Телепорт ${i+1} использован, заряд — 0 единиц, требуется перезарядка!`);
			} else {
				teleportCharge[i]--;
				console.log(`Телепорт ${i+1} использован, заряд — ${teleportCharge[i]} единиц`);
			}
		};
	}

	return function (teleportNumber) {
		updateCharge[teleportNumber - 1]();
	};
}

var usedTeleport = chargeUpdater();
usedTeleport(1);
usedTeleport(1);
usedTeleport(2);
usedTeleport(2);
usedTeleport(3);
usedTeleport(3);