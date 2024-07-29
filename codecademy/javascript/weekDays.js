let weekDays01 = ['mon', 'tue', 'wed', 'tur', 'fry', 'sat', 'sun'];
let arraySize = weekDays01.length;
let randomChoice = Math.floor(Math.random() * arraySize);
let randomReturn = weekDays01[randomChoice];
console.log(randomReturn);