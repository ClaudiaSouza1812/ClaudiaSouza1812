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