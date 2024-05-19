
//in this code, we will receive a full name of a costumer, after that, we will print the type of the information inserted. Further, we will use an if else statement to check if the values are strings, if they did, we will print the full name, if dont, we will print a message asking the user to review the information inserted.
let firstName = 5;
let middleName = 'Simone';
let lastName = 'de Souza';
let fullName = firstName + ' ' + middleName + ' ' + lastName;

console.log(typeof firstName);
if(typeof firstName !== "string" || typeof middleName !== "string" || typeof lastName !== "string"){
  console.log('Please, check your name, its dosen\'t must have numbers or symbols');
} else {
  console.log(fullName);
}