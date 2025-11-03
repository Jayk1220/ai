//false로 간주되는 값 : 0, '', NaN, null, undefined  cf. []는 True

var i;
console.log(Boolean(i));
console.log(Boolean(0));
console.log(Boolean(Nan));
console.log(Boolean(Number('a')));
console.log(Boolean(''));
console.log(Boolean(''));
console.log(Boolean(null));
console.log();
console.log('0==false의 결과 : ', 0==false);
console.log('0===false의 결과 : ', 0===false);
