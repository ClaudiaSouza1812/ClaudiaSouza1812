












































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
