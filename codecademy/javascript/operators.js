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
  