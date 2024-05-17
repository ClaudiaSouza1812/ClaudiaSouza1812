
//the first line of this code has a constant variable (wich its content can´t be changed further) with the name Kelvin refering to the temperature scale, it has 293 as a value;
//the next one its a constant that stores the celsius temperature, for that its calculate the kelvin value minus the difference in celsius degree;
//the next one its a let variable (wich can have its value changed further) that stores the fahrenheit temperature, result of a calculus that considers celsius degree;
// for last but not less important, we have another let variable that stores de newton degree as a result of a calculus consideriyng the celsius degree;
//for the fahrenheit and newton degrees we certantly will have a decimal result, for that matter we can see a integer number if we use a Math object with the .floor() method, this way changiyng the result;
//the next step is to print the fahrenheit and newton degrees using a string interpolation;

const kelvin = 263;
const celsius = kelvin - 273;
let fahrenheit = celsius * (9/5) + 32;
let newton = celsius * (33/100);

fahrenheit = Math.floor(fahrenheit);
newton = Math.floor(newton);
console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);
console.log(`The temperature is ${newton} degrees Newton.`);

