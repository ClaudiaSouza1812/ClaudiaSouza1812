
// my age
//sotorage de early years number, that will certanly change
//multipliyng early years by 10.5
//creating a new variable and subtracting myAge by 2;
//multipliyng my years for a dog years
//imprimindo early years and later years
//storing my dog years in a new variable
//putting my name in a string and using a string method to change the letters to upper case
//printing my name, my age in human and dog years

let myAge = 41;
let earlyYears = 2;
earlyYears *= 10.5;
let laterYears = myAge - 2;
laterYears *= 4;
console.log(`the early years are ${earlyYears} and the later years are ${laterYears}.`);
let myAgeInDogYears = earlyYears + laterYears;
let myName = 'Claudia Souza'.toUpperCase();

console.log(`My name is ${myName}. I am ${myAge} years old in human years, which is ${myAgeInDogYears} years old in dog years.`);

//putting Mel dogs age in a variable
//calculating the first two years of a dog in human years
//adjusting Mel dogs age subtraing the first two years
//calculating the further years of Mel human age
//calculating Mel years in human years by sum firstYears and furtherYears variables
//printing Mels age in dog and human years;

let melAge = 12;
const firstYears = 2 * 10.5;
let melAgeAdjust = melAge - 2;
const furtherYears = melAgeAdjust * 4;
let melHumanYears = firstYears + furtherYears;

console.log(`Mel has now ${melAge} years old in dog years an has ${melHumanYears} years old in Human years.`);
