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

//variaveis let
var word = 'esse é';
console.log(word);
for (let word of 'um teste'){
  console.log(word);
}
console.log(word);


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
