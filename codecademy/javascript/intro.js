
//Function: A function tells a computer to do a certain thing. Functions can take arguments to give the computer extra information. For example drawBox(red) its a function that has red as an argument, telling the computer to draw a red box.

console.log('estou aprendendo a programar, é muito legal!');

//Argument: An argument is extra information given to a function that tells it how it should run.

console.log('desta vez o argumento é um argumento... :)');

//String: Letters, words, and sentences are called strings in coding. Quotation marks ('')  are used to show the start and end of a string. For example, 'hello world' is a string.

console.log('se tem aspas, é string!');

//Variables: Variables are very common in coding. They allow you to reference the same piece of information multiple times. In JavaScript, variables can be defined using the word "var" then giving the variable a unique name. For example, var myVariable = 'some text'. The variable can later receive a new value. For example, myVariable = 'changed some text' When reassigning a variable the word "var" is not necessary anymore. The variable myExample is declared, then on the next line it's given a value and is then printed out. The variable's value is then updated and printed out again with a different message.

var guerreira = 'Claudia Simone de Souza';
console.log('print the name of the most brave person that you know: ' + guerreira + ':)');
guerreira = 'Paula de Fátima Vallim Magalhães';
console.log('who are your inspiration to be brave? ' + guerreira);

//Arguments are placed inside the parentheses of a function call. Not all functions require arguments, and some functions take multiple arguments.

//equal sinal (=): Sets (or resets) the value stored in a variable. On the left is the variable you'd like to adjust, and on the right is the new value.

/*The sinals / * + and - will work on the value associated with the variable on the left by the value on the right, and assigns the resulting value to the existing variable.
var myNumber = 10;
myNumber /= 5;
So, the var myNumber will bring the value 2 now, cause 10 divided by 5 is equal to 2.
*/

//no exemplo abaixo,
var x = 19;
var y = 20;
var age = x + y;
console.log('my age is', + age);


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

//opening line
console.log('It has been lovely at first sight.');
/*the bottom 6 lines commented with success ;)
console.log('The first time Yossarian saw the chaplain he fell madly in love with him.');
console.log('Yossarian was in the hospital with a pain in his liver that fell just short of being jaundice.');
console.log('The doctors were puzzled by the fact that it wasn\'t quite jaundice.');
console.log('If it became jaundice they could treat it.');
console.log('If it didn\'t become jaundice and went away they could discharge him.');
console.log('But this just being short of jaundice all the time confused them.');
*/

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

//Um laço for of: repete a seção de código entre chaves {}. Em JavaScript, um laço for of percorre cada elemento em uma array ou string, repetindo o código para cada elemento. Cada item na string 'codecademy' será impresso em sua própria linha.
for (var spellWords of 'Codecademy') {
  console.log(spellWords);
};

var message = 'im not very well today';
console.log(message.replace('not','really'));

//Laço while: executa o código dentro de seu bloco até que o teste entre parênteses não seja mais verdadeiro. Contanto que "a" seja menor que 3, o código no bloco de comandos será repetido. Se você esquecer de aumentar "a" neste código, o laço while se repetirá para sempre e causará uma falha.
let a = 0;
while (a < 3) {
    console.log('a is ' + a + ', less than 3');
    a++;
};
console.log('a is now 3!');

//variaveis let
var word = 'esse é';
console.log(word);
for (let word of 'um teste'){
  console.log(word);
}
console.log(word);

//if...else statements: perform a test to decide which code to run. If the test is true, the if block {} runs. If the test is false, the else block {} runs.
var x = 8;
console.log(x);
if (x > 5){
  let x = 1
    console.log(x);
} else {
    let x = 0
     console.log(x)
}

//operador ternario
var x = 6;
x > 10 ? console.log('its bigger than 10') : console.log('its lowest than 10');

//operador de incremento e decremento
var x = 10;
console.log('o valor é ' + x);
x++;
console.log('o valor atualizado é ' + x);
x--;
console.log('saldo final ' + x);

//atribuição de adição e de subtração
let antAnna = 40;
let grasshopper = 0;
let gift = 10;
antAnna -= gift;
grasshopper += gift;
console.log('the ant Anna has ' + antAnna + ' seeds ' + 'and the grasshopper has ' + grasshopper + ' seeds for the winter');

//declarações de funções
function inYen(dollar){
  let amount = dollar * 113;
    return amount;
};
  console.log('the exchanged amount is ' + inYen(100));

//declarações de funções: nesta declaração, determinamos que o valor inserido em wallet, em seguida, criamos uma função chamada exchangeToReal, ela  possui um argumento que determina que o valor que está dando entrada é em dollar, por isso se chama dollar. Na sequência, criamos a fórmula que esta declaração rodará, nela declaramos uma varivel do tipo "let" com o nome da moeda a ser cambiada, que retornará o valor do dólar vezes o valor equivalente a moeda, então saberemos que toda vez que a função exchangeToReal for chamada, será feito o cambio de dollar para real.
let wallet = 1000;
function exchangeToReal01 (dollar) {
  let real = dollar * 5.42;
   return real;
};
function exchangeToReal02 (euro) {
  let real = euro * 5.45;
  return real;
};
function exchangeToDollar (real){
  let dollar = real / 5.42;
  return dollar;
};
function exchangeToEuro (real){
  let euro = real / 5.45;
  return euro;
};
console.log('the amount of ' + wallet + ' dollares exchanged to Real is ' + exchangeToReal01(wallet) + ' reais');
console.log('the amount of ' + wallet + ' euros exchanged to Real is ' + exchangeToReal02(wallet) + ' reais');
console.log('the amount of ' + wallet + ' reais exchanged to Dollar is ' + exchangeToDollar(wallet) + ' dolares');
console.log('the amount of ' + wallet + ' reais exchanged to Euro is ' + exchangeToEuro(wallet) + ' euros');

//chamada de função dentro de uma declaração de função: A função 'bigger' é a primeira função criada, nela o teste 'if else' é inserido, ele testará se o valor de 'a' é maior que 'b', se sim, imprimirá 'a', senão, imprimirá 'b'. Depois, a função 'maximum' também é criada, nela não é preciso haver argumento entre parenteses, apenas a ação a ser executada entre colchetes, neste caso, uma variavel 'max' é criada com valor '0', apenas para servir de comparação com a variavel que será criada dentro da proxima no laço 'for of'. A função 'for of' é um laço que percorrerá item por item de uma lista ou string e poderá imprimir cada item em sua prórpia linha se a função 'console.log' for utilizada. Na função 'for of' a variável 'num' é criada, ela é a 'chamada' no laço, que fará a função percorrer todos os elementos da variavel 'list', criado anteriormente. Em seguida, ocorre a 'chamada' da função 'bigger' dentro do bloco de códigos do laço. Neste caso específico, os argumentos 'a' e 'b' da função 'bigger' são preenchidos pelas variáveis 'max' e 'num', a função 'max' trará o valor '0' determinado e a 'num' testará todos os numeros da lista, até que o maior numero seja encontrado.

let list = [54,  27,  93,  78,  11];
function bigger (numOne, numTwo){
  return numOne > numTwo ? numOne : numTwo;
};
function maximum (){
  let maxNum = 0;
  for (let pickNum of list){
    maxNum = bigger(maxNum, pickNum);
  };
   return maxNum;
};
console.log(list);
console.log(maximum());


let weekDays01 = ['mon', 'tue', 'wed', 'tur', 'fry', 'sat', 'sun'];
let arraySize = weekDays01.length;
let randomChoice = Math.floor(Math.random() * arraySize);
let randomReturn = weekDays01[randomChoice];
console.log(randomReturn);

let groceries = ['apples', 'yogurt', 'toothpaste'];
let arraySize01 = groceries.length;
let randomChoice01 = Math.floor(Math.random() * arraySize01);
let randomReturn01 = groceries[randomChoice01];
console.log(randomReturn01);

let choices = ['a', 'b', 'c']
let tamanho_array = choices.length
let n_aleatorio = Math.floor(Math.random() * tamanho_array);
let retorno_aleatorio = choices[n_aleatorio]
console.log(retorno_aleatorio);


let choice03 = '2';
for (let item of choice03){
  item === '3' ? console.log('you have selected your item') : console.log('you dont have selected items')
};

for (var element of [1,2,3,4,5]){
  console.log(element);
}

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

let aa = 95;
while (aa < 100){
  aa++;
console.log(aa);
};

console.log(38 + 3.5);
console.log(2022 - 1982);
console.log(65 / 240);
console.log(0.2708 * 100);


//The 'remainder' operator (%), sometimes called 'modulo', returns the number that remains after the right-hand number divides into the left-hand number as many times as it evenly can: 11 % 3 equals 2 because 3 fits into 11 three times, leaving 2 as the remainder.
console.log(11 % 3);
console.log(15 % 8);
console.log(12 % 3);

console.log('Hello' + 'World');
console.log('Hello' + ' ' + 'World')

console.log('Teaching the world how to code'.length);

// Use .toUpperCase() to log 'Codecademy' in all uppercase letters
console.log('Codecademy'.toUpperCase());

// Use a string method to log the following string without whitespace at the beginning and end of it.
console.log('    Remove whitespace   '.trim());

//Objeto Math: para operações metematicas mais complexas. Os objetos possuem métodos variados, cada um deles executa uma determinada função, .random() por exemplo, irá escolher um númeroa aleatório entre 0 e 1, para escolha de numeros acima de 0 e 1, basta utilizar o sinal * e declarar o range máximo ao lado, assim: Math.random()*100. O método .floor irá pegar um número decimal e o arredonda para baixo para o número inteiro mais próximo para garantir que o número escolhido seja um número inteiro e não decimal. O método .ceil retorna numero inteiro maior ou igual ao numero decimal declarado entre parenteses.
console.log(Math.floor(Math.random() * 100));
console.log(Math.ceil(42.8));
console.log(Number.isInteger(2017.2));

//Um objeto pode armazenar várias informações dentro de uma variável. A notação de ponto é usada para acessar uma propriedade de um objeto. Por exemplo, name.first. Um objeto armazena vários valores que possuem nomes de propriedade (ou chave). Isso permite que eles sejam facilmente acessados posteriormente no código. First, middle e last são propriedades do objeto name. Claudia, Simone e de Souza são os valores associados a essas propriedades. name.first, por exemplo, é igual a Claudia.
var name = {
  first: 'Claudia',
  middle: 'Simone',
  last: 'de Souza',
};
console.log(name.first + ' ' + name.middle + ' ' + name.last);

var myBackpack = {
  food: 'bananas',
  equipment: 'map',
  clothing: 'hat',
};
console.log(myBackpack.food);

var myBackpack = {
  food: [
    'apples',
    'bananas',
    'pineapples',
    ],
  clothing: [
    'hat',
    'pants',
    'shirts',
    ],
  equipment: [
    'map',
    'flashlight',
    'lighter',
    'rope',
    ],
};
console.log(myBackpack.food);
console.log(myBackpack.clothing);
console.log(myBackpack.equipment);

for (var element of myBackpack.food){
  console.log(element);
  };
for (var element of myBackpack.clothing){
  console.log(element);
};
for (var element of myBackpack.equipment){
  console.log(element);
};

//no exemplo abaixo, um laço for of é usado para verificar quais são os itens armazenados na variavel myBackpack, que contém um objeto {} com várias propriedades, entre elas, a propriedade equipment, que carrega consigo vários valores, são eles: 'map', 'flashlighter','lighter'. O laço roda a função console.log para imprimir os valores contidos em myBackpack.equipment através da chamada da variavel element como argumento. Um laço repete a seção de código entre chaves {}. Em JavaScript, um laço for of percorre cada elemento em uma array ou string, repetindo o código para cada elemento.

for (var element of myBackpack.equipment){
  console.log(element);
};

var bill = Math.random() * 500;
var payment = {
  money:[
    10,
    20,
    30,
    40,
  ],
  ticket:[
    50,
    60,
    70,
    80,
    90,
  ],
  creditCard:[
    100,
    150,
    200,
    300,
    400,
    500,
  ],
};
console.log(bill);
if (bill <= 40){
  console.log('The cliente can pay with money because the bill is in the range: ' + payment.money);
};
if(bill >= 100){
    console.log('The client can pay with Credit Card because the bill is in the range: ' + payment.creditCard);
}
if (bill > 40 && bill < 99){
console.log('The client can pay with ticket because the bill is in the range: ' + payment.ticket)
};


for (var element of myBackpack.equipment){
  if (element === 'rope'){
    console.log('the rope was found');
  } else {
    console.log('rope wasnt found, there are: ' + element);
  }
};

var message = 'estou aprendendo a codificar e estou gostando!!!';
console.log(message);
if (message.lenght > 10){
  console.log("this message dosen't fits in a postcard");
} else {
  console.log('this message fits in a postcard');
};

//Método de inclusão: quando o método .includes() é aplicado a uma string (ou array), ele verifica se o valor entre parênteses pode ser encontrado dentro da string (ou array). Retorna verdadeiro se encontrar o valor e falso se não encontrar. O método .includes() pode ser usado em uma string para verificar se ela contém um valor específico. Por exemplo, 'I love coding'.includes('love') pesquisa a string 'I love coding' para o argumento 'love'. Como a frase 'I love coding' contém 'love', todo o comando retorna true.

var chat = [
  'bye',
  'hello',
];
if (chat.includes('hello')){
  console.log('hello! How can i help you today?');
}
if(chat.includes('bye')){
  console.log('thanks for calling us, well be here when you must buy something');
}
console.log('hello world'.includes('hello'));

//Método .replace(): procura um valor e, se o encontrar, substituirá o 1º valor por uma nova string. Por exemplo, para mudar a string 'lemons' em 'lemonade', você usaria .replace('lemons', 'lemonade').

var message = 'today we are going shopping';
console.log(message);
message = message.replace('day', 'morrow');
console.log(message);

var message = 'Claudia, you beautiful and smart girl!';
console.log(message);
message = message.replace('beautiful','gorgeous');
console.log(message);

//Variáveis declaradas com let: Às vezes, é necessário manter as variáveis separadas, para garantir que não sejam alteradas por engano, variáveis let não podem ser usadas fora do bloco de código onde vivem. A variável declarada com var não foi afetada pela outra variável declarada com let, embora tivesse o mesmo nome.

var text = 'hello';
console.log(text);
for (let text of [
  'hi',
  'oi',
]) {
  console.log(text);
}
console.log(text);

//let declara uma variável como var, exceto que tem um escopo diferente. O escopo de uma variável é a seção do código onde ela pode ser usada. Um let só pode ser usado dentro do bloco de código {}onde é criado. Uma variável chamada x é criada usando var e definida como 100. A if statement é verdadeira, então a variável let x é criada e definida como 25. A variável let permanece dentro do bloco de código {}. A console.log(x), que está fora do bloco de código da if statement, usa o valor de var x = 100.

var x = 100;
if (x > 0) {
    let x = 25;
}
console.log(x);

//operador ternário: usa um ponto de interrogação ? E dois pontos : para substituir uma if...else statement inteira por uma única linha de código. Por exemplo: test ? doThisIfTrue : elseDoThis. Eles começam com o teste e, depois do símbolo ?, é o código rodado se o teste for verdadeiro. A última parte, após o símbolo :, é o código que será rodado se o teste for falso. Veja um exemplo de uma if...else statement testando se 1 é igual a 1; e o mesmo código usando um operador ternário.


if (1 === 1){
  console.log('thats ok');
} else {
  console.log('something is wrong');
}
 1 === 2 ? console.log('thats ok') : console.log('something is wrong');

 var timeOffwork = 7;
 var daysNeeded = 5;
 var car = 2;
 var train = 3;
 timeOffwork > daysNeeded ? console.log('go on vacation') : console.log('comeback to work');
 car < train ? console.log('drive a car') : console.log('buy train tickets');

//O operador de incremento ++ adiciona 1 a uma variável, enquanto o operador de decremento -- subtrai 1. Por exemplo, count++ é igual a count = count + 1.

let x10 = 10;
x10++;
console.log(x10);
x10--;
console.log(x10);

//operadores atribuição de adição e atribuição de subtração: O operador += adiciona o valor associado à variável à esquerda ao valor à direita, o operador -= subtrai o valor associado á variavel esquerda ao valor a direita, ao final atribuem o valor resultante à variável existente.

var ant = 40;
var grasshopper01 = 0;
var gift01 = 10;
ant -= gift;
grasshopper += gift;
console.log('ant has ' + ant + ', grasshopper has now ' + gift);

//Declaração de função: Uma função salva um bloco de código. É possível executá-lo sempre que fizer referência ao nome da função. O código dentro do bloco {} será rodado quando o nome da função for chamado. A palavra-chave function cria uma nova função chamada inYen que receberá um argumento nos parenteses. Nos colchetes será determinada a ação a se realizar com esse argumento, para tanto é necessário criar uma variável para tratar o argumento, amount, ela será igual ao argumento vezes o valor necessário para retornar o valor em Yenes. Depois da variável é necessário utilizar a palavra-chave return, pois, quando uma função é concluída, a saída pode ser enviada de volta para o local de onde foi chamada. Para isso, é usada a palavra-chave return.

function inYen(dollars){
  let amount = dollars * 113;
  return amount;
}
console.log(inYen(10));

function inRealtodollar(dollars){
  let amount = dollars*5.3;
  return amount;
}
console.log(inRealtodollar(10));

function inDollar(real){
  let amount = real / 5.3;
  return amount;
}
console.log(inDollar(10));

function inEuro(real){
  let amount = real / 6.3;
  return amount;
}
console.log(inEuro(10));

function inRealtoeuro(euro){
  let amount = euro*6.3;
  return amount;
}
console.log(inRealtoeuro(10));


var wallet01 = 50;
function inBath(dollars){
  let bath = dollars*33;
  return bath;
}
console.log('you have ' + wallet + ' Dollars');
console.log('your amount exchanged to Baths is ' + inBath(wallet) + ' Baths');


function half(value){
  return value / 2;
}
let c = 8;
console.log(half(c));


var list01 = [
  10,
  20,
  30,
  40,
  50,
];

function larger(a, b){
  return a > b ? a : b;
};

function maximum(lst){
  let max = 0;
  for (let num of lst){
    max = larger(max, num);
  }
  return max;
};

console.log(list01);
console.log(maximum(list01));

//Recursão: Recursão é quando uma função chama a si mesma dentro de seu próprio código de execução.
//Substituição de recursão: no código abaixo, a função updateAllnames receberá 3 argumentos que serão submetidos ao código entre colchetes. Dentro dos colchetes há uma if statement que testa através do método .includes se o argumento string possui algum elemento do argumento oldPart, se possuir, será igual a false, portanto, o código entre colchetes da if statement não será executado, as if statements permitem que você execute uma seção específica do código somente quando um teste for verdadeiro. O código entre parênteses () é o teste, se o teste for verdadeiro, o código dentro do bloco {} será executado, se o teste não for verdadeiro, o código não será executado, ou sejá, não retornará a string e passará ao próximo código, nele haverá o uso do métrodo .replace para substituir a oldPart pela newPart, após a substituição, retorna a função updateAllNames com a string modificada e os argumentos mantidos, para que cheque novamente se ainda há algum erro. Na if statement será atestado que a string não possui mais a oldPart, assim, o resultado será verdadeiro, o que executará o código entre colchetes que pede para retornar a string modificada, neste momento, a função para de chamar a si mesma, pois sua condição foi alcançada, ou seja, condição de não haver mais erros. Na sequencia, a string contida em travelDoc é impressa, ao perceber os erros no texto, o usuário chama a função updateAllNames capaz de corrigi-los, para tal, utiliza as variáveis que armazenam as informações inseridas, travelDoc, wrongPart e rightPart, fazendo toda a checagem e correção, se necessário.
var travelDoc = 'este é um quebra cabeças';
var wrongPart = 'este é';
var rightPart = 'isto não é';

function updateAllNames(string, oldPart, newPart){
if (string.includes(oldPart) === false){
  return string;
} else {
  string = string.replace(oldPart, newPart);
  return updateAllNames(string, oldPart, newPart);
}
}

console.log(travelDoc);
console.log(updateAllNames(travelDoc, wrongPart, rightPart));

//A função ftl pega um número n e multiplica por todos os números inteiros antes dele. Portanto, o ftl(3) é 3 2 1. Cada vez que essa função efetua a recursão, ela subtrai 1 do valor do argumento até que o caso básico de n === 1 seja encontrado. ftl(3)→(3 * ftl(2)) ftl(2)→(2 * ftl(1)) ftl(1)→ 1 Portanto, ftl(3) retorna (3 * ( 2 * (1))) que é 6.

function ftl(n){
  if (n === 1){
    return 1;
} else {
  return n * ftl(n - 1);
}
};

console​.log(ftl(3));


let listOfDestinations = [
  'São Paulo',
  'Lisboa',
  'Londres',
  'Paris',
  'Madrid',
  'Roma',
];
let numberOfDestinations = listOfDestinations.length;
console.log('There are ' + numberOfDestinations + ' destinations to pick');

//O método .slice() cria uma nova array copiando uma subseção de outra array. São necessários 2 argumentos: um índice de array onde começar a copiar e um índice onde terminar (numero fim não incluído).
let cities = [
  'Porto',
  'London',
  'Lisboa',
  'Paris',
  'Madrid',
  'Roma',
  'Washington',
  'Nova York',
  'Miami',
  'Cidade do México',
  'Ottawa',
  'Toronto',
  'Montreal',
  'Vancouver',
  'São Paulo',
  'Santiago',
  'Buenos Aires',
  'Montevidéo',
  'Asunción',
];
let transportation = [
  'train',
  'airplane',
  'bus',
  'boat',
];
console.log(cities.slice(6,13));
console.log(transportation.slice(0,5));


let departures = [
  ...cities
];
for (let element of cities){
  console.log(element);
};
console.log('the list has ' + cities.length + ' destinies');


var myArray = [
  'oranges',
  'apples',
  'bananas',
  'carrots',
  'milk',
  ];
  var newArray = myArray;
console.log(newArray.slice(1,3));

//Método .push: Adiciona um valor ao final de uma array.
let travelToCities = [
  southAmerica = {
    destination : 'São Paulo',
    transportMode : 'airplane',
    cost : 200.00,
    country : 'Brazil',
  },
  europe = {
    destination : 'Porto',
    transportMode : 'boat',
    cost : 150.00,
    country : 'Portugal',
  },
  asia = {
    destination : 'Toquio',
    transportMode : 'boat',
    cost : 90.00,
    country : 'Japão',
  },
  northAmerica = {
    destination : 'New York',
    transportMode : 'bus',
    cost : 100.00,
    country : 'EUA',
  },
];
let lastTravel = travelToCities[travelToCities.length - 1];
console.log(lastTravel.destination);

let africa = {
    destination : 'Joanesburg',
    transportMode : 'airplane',
    cost : 250.00,
    country : 'South Africa',
};

travelToCities.push(africa);
lastTravel = travelToCities[travelToCities.length - 1];
console.log(lastTravel.destination);
console.log('your last travel was to ' + lastTravel.destination + ' with te cost of ' + lastTravel.cost + ' US dollars with ' + lastTravel.transportMode + ' as transportation to the country of ' + lastTravel.country);

//O método .pop() remove o último item em uma array para editá-lo, após a edição usaremos o método .push() para colocá-lo de volta. Os itens desta array são objetos e cada um tem 4 propriedades: destination, transportMode, cost e country. O último objeto da array é “laçado” e armazenado em uma variável chamada africaTravel. Este é o objeto que você adicionou na lição anterior. Em seguida, a propriedade transportMode é alterada para 'hovercraft'. Agora que o objeto foi editado, é possível adicioná-lo de volta ao final da array usando .push(). Você precisará usar travelToCities.push(africaTravel) para fazer isso. O código a seguir armazena o último elemento da array em uma variável chamada lastOne. Isto será o mesmo que o objeto africaTravel, pois você acabou de inclui-lo na array.

let africaTravel = travelToCities.pop();
africaTravel.transportMode = 'hovercraft';
travelToCities.push(africaTravel);
let lastOne = travelToCities[travelToCities.length - 1];
console.log(lastOne.destination);
console.log(lastOne.transportMode);

console.log(obsolateOne);

var obsolateOne = false;
let learningToCode = 'fun';
const doingTheTest = 10;
let mixVariables = doingTheTest + obsolateOne;

console.log(obsolateOne + ' ' + learningToCode + ' ' + doingTheTest);
console.log(`what do you thing about coding? ${learningToCode}. How do you think about you are going? Give to your self a note in the range of 0 and 10 - ${doingTheTest}. And what do you think about the var variable after this lesson? ${obsolateOne}`);

//typeof operator: While writing code, it can be useful to keep track of the data types of the variables in your program. If you need to check the data type of a variable’s value, you can use the typeof operator.The typeof operator checks the value to its right and returns, or passes back, a string of the data type.

console.log(typeof obsolateOne);
console.log(typeof learningToCode);
console.log(typeof doingTheTest);
console.log(typeof mixVariables);

/*Objetivo: Filtrar departures para obter os horários antes e após o meio-dia e armazená-los em eveningTimes e morningTimes. Passo a passo da solução:
Departures é uma array de strings, cada string é um número seguido de 'am' ou 'pm'.
As funções morning e evening são criadas e recebem um argumento (array), depois, em seus blocos {}, rodam o método .includes(), que percorre cada item da lista e verifica se contém 'am' e 'pm' como valor, retornando true e/ou false.
O método .filter() aplica um teste a cada elemento em uma array e retorna uma nova array que contém apenas os elementos que retornam true.
As variáveis morningTimes e eveningTimes são criadas para armazenar separadamente os horários da manhã e da noite contidos na array departures, para tanto, chamam a variável departure e aplicam os métodos que se seguem.
Quando o método .filter() é aplicado a departures e usa como argumento as funções criadas, elas rodam o .include() na array e classificam quais elementos são true e false, na sequencia, o .filter() pode então filtrar apenas os elementos classificados como true, pois, se a verificação for falsa, não passa no filtro.
Quando o console loga morningTimes, somente os elementos que incluam 'am' são impressos, o mesmo ocorre com eveningTimes, imprimindo apenas itens com 'pm'*/

let departures = [
  '8pm',
  '9pm',
  '10pm',
  '11pm',
  '8am',
  '9am',
  '10am',
  '11am',
];
function morning(array){
  return array.includes('am');
};
function evening(array){
  return array.includes('pm');
};
let morningTimes = departures.filter(morning);
let eveningTimes = departures.filter(evening);
console.log(morningTimes);
console.log(eveningTimes);
