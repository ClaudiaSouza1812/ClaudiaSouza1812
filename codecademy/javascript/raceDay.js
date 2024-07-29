
//in this project we will generate randomly a competicion number for runners that registered early or not. First of all, we declare a variable that generate a number using math.floor to sure a integer number, in its argument we will use a math.random to choose randomly a number until 1000. Now we will create a variable that tells if a runner is registered early with a boolean value as a answer. Now we create a variable thats receive the runners age, after that, we will add a 1000 to the number of runners that registered early and have more than 18 years. Right after, we will do the control flow using a if else if statement that checks the register, the ages and return a console.log accordanly with the test.

//generate a integer random number:
let raceNumber = Math.floor(Math.random() * 1000);
//says if the early register is true or false (bollean):
let regEarly = true;
//receive the runners ages:
let runAge = 19;
//add 1000 to the runner number if they registered early anh have more than 18 years:
if (regEarly && runAge > 18) {
  raceNumber += 1000;
} 
//if reg early and 18 plus, console.log:
//if dont reg early and 18 plus, console.log:
//if less then 18 years, console.log:
//else ecxacly 18 yeras, console.log:
if (regEarly && runAge > 18) {
  console.log(`Runner ${raceNumber}, you will race at 9:30am`);
} else if (!regEarly && runAge > 18) {
  console.log(`Runner ${raceNumber}, late adults run at 11:00 am`);
} else if (runAge < 18 ) {
  console.log(`Runner ${raceNumber}, youth registrants run at 12:30 pm (regardless of registration)`);
} else {
  console.log('Runners with exactly 18 years, please go to the registration desk');
}