
//In this project, we need to write a code were a user, identifyied or not, will ask a question, after that will the user press a button that will return a random number, each number will be use by the entit named "Eight Ball" to predict the probable answer;
//right bellow the switch option:
let userName = 'Jane';
userName ? console.log(`Hello ${userName}`) : console.log('Hello!');

let userQuestion = 'I\´d like to know if someday i will be a milionare?';
console.log(`${userName} is asking: ${userQuestion}`);

const randomNumber = Math.floor(Math.random() * 8);
let eightBall = '';
switch (randomNumber) {
  case 0:
    eightBall = 'It is certain';
    break;
  case 1:
    eightBall = 'It is decidedly so';
    break;
  case 2:
    eightBall = 'Reply hazy try again';
    break;
  case 3:
    eightBall = 'Cannot predict now';
    break;
  case 4:
    eightBall = 'Do not count on it';
    break;
  case 5:
    eightBall = 'My sources say no';
    break;
  case 6:
    eightBall = 'Outlook not so good';
    break;
  case 7:
    eightBall = 'Signs point to yes';
    break;
}
console.log(randomNumber);
console.log(`The Eight Ball return the following message to you: ${eightBall}`);

//right bellow an if else and else if option:
let userName1 = 'Flora';
userName1 ? console.log(`Hello ${userName1}`) : console.log('Hello!');

let userQuestion1 = 'I\´d like to know if someday i will be a milionare?';
console.log(`${userName1} is asking: ${userQuestion1}`);

const randomNumber1 = Math.floor(Math.random() * 8);
let eightBall1 = '';

if (randomNumber1 === 0) {
  eightBall1 = 'It is certain';
  } else if(randomNumber1 === 1) {
    eightBall1 = 'It is decidedly so';
  } else if(randomNumber1 === 2) {
    eightBall1 = 'Reply hazy try again';
  } else if(randomNumber1 === 3) {
    eightBall1 = 'Cannot predict now';
  } else if(randomNumber1 === 4) {
    eightBall1 = 'Do not count on it';
  } else if(randomNumber1 === 5) {
    eightBall1 = 'My sources say no';
  } else if(randomNumber1 === 6) {
    eightBall1 = 'Outlook not so good';
  } else if(randomNumber1 === 7) {
    eightBall1 = 'Signs point to yes';
  } 
  
console.log(randomNumber1);  
console.log(`The Eight Ball return the following message to you: ${eightBall1}`);