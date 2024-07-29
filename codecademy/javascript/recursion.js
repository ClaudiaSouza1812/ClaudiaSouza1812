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
