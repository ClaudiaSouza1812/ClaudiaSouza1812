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
  