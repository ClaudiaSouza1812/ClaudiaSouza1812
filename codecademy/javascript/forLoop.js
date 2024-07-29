
//Laço for of: repete a seção de código entre chaves {}. Em JavaScript, um laço for of percorre cada elemento em uma array ou string, repetindo o código para cada elemento. Cada item (strings) da array abaixo será impresso em sua própria linha.

console.log('the days of a week are: ');
var weekDays = [
  'monday', 'twesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'sunday'
]
for (var element of weekDays){
console.log(element)
};


var collor = [
  'yellow',
  'blue',
  'red'
]
for (var element of collor){
console.log(element)};

//If statements: its a function that allow you to run a specific section of code when a test is true. The code inside the parentheses () is the test. If the test is true, then the code inside the block {} runs. If the test is not true, then the code inside the block doesn't run.
var tollBox = [
  'nail',
  'hammer',
  'pliers',
  'sow',
  'screw',
];
for (var element of tollBox){
console.log(element)
};
 if (tollBox === 'hammer','nail','pliers','sow','screw'){
console.log('you are abble to do your job')
};


  var ingredients = [
    'milk',
    'flour',
    'suggar',
    'salt',
    'eggs',
    'yeast'
  ];
  var cake = 'you can make a cake';
  var fail = 'ingredients are missing, check your list';
  for (var element of ingredients){
    console.log(element)
  };
    if (ingredients === 'milk','flour','suggar','salt', 'eggs','yeast'){
    console.log(cake)
    }
    else {
      console.log(fail)
      };

var colorBananas = 'yellow';
var numberBananas = 8;
if(colorBananas === 'yellow' && numberBananas === 10){
      console.log('we have a entire bunch of ripe bananas')
  }
else {
  console.log('we dont have your wish')
  };


for (var fullWord of 'teste') {
  console.log(fullWord);
  }

for (var color of [
  'red',
  'blue',
]) {
  console.log(color);
}

for (var x = 0; x < 10; x = x + 2){
console.log(x)}

var message = 'hello, im going into your way';
console.log(message);
if (message.length < 25) {
  console.log('the message fits on a postcard');
}
else {
  console.log('you need to wrote less words');
}

console.log('do you want to travel?');
var chat = 'yes';
if(chat.includes('yes')){
  console.log('great! pickup your destination!');
} else {
  console.log('weel, we will be right here when you want to travell');
}

console.log('JavaScript');
console.log(2011);
console.log('Woohoo! I love to code! #codecademy');
console.log(20.49);

var colors = [
  'black',
  'white',
  'yellow',
  'blue'
];
console.log(colors[0]);
console.log(colors[2]);
console.log(colors[1]);
console.log(colors[3]);
console.log(colors[1]);
console.log(colors[0]);

//Laço 'for' clássico: repete o mesmo código dentro do bloco {} um número determinado de vezes. Ele é definido em três partes. A primeira parte acontece antes do início do laço e define uma variável de laço (var i = 0;). A segunda parte é um teste que determina se o laço deve continuar se repetindo (i < 10;). E a terceira parte atualiza a variável do laço cada vez que ele se repete (i = i + 1). Neste exemplo, a variável do laço (i) começa em 0. O código no bloco {} continuará se repetindo enquanto i for menor do que 10. E i é aumentado em 1 a cada laço. Esse código imprime os números de 0 a 9.

for (var i = 0; i < 10; i = i + 1){
    console.log(i);
  };
  console.log('the loop will go as long as i is less than 10​.');
  
  //neste exemplo, temos uma contagem regressiva
  for (var i = 10; i > 0; i = i - 1) {
    console.log(i);
  }
  console.log('Happy New Year!');
  
  //Laços aninhados: é um laço dentro de outro laço. Embora os laços aninhados possam ser úteis, se você tiver muitos, pode tornar a execução do código lenta ou difícil de entender.
  for (var name of ['inventores', 'matadores', 'construtores']){
    for (var secName of ['do tempo', 'da vida', 'da bagaça']){
      console.log('Os ' + name + ' ' + secName);
    };
  };
  //Esse código imprimiria 1,6, e 1,7. E então outerNumber mudará para 2, e o laço interno imprimirá 2,6, depois 2,7 e assim por diante.
  for (var outerNumber of [1, 2, 3]) {
      for (var nestedNumber of [6, 7,]) {
          console.log(outerNumber, nestedNumber);
      };
  };