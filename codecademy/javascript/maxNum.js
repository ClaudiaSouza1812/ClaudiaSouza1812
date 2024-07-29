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