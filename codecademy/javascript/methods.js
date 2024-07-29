console.log('Teaching the world how to code'.length);

// Use .toUpperCase() to log 'Codecademy' in all uppercase letters
console.log('Codecademy'.toUpperCase());

// Use a string method to log the following string without whitespace at the beginning and end of it.
console.log('    Remove whitespace   '.trim());

//Objeto Math: para operações metematicas mais complexas. Os objetos possuem métodos variados, cada um deles executa uma determinada função, .random() por exemplo, irá escolher um númeroa aleatório entre 0 e 1, para escolha de numeros acima de 0 e 1, basta utilizar o sinal * e declarar o range máximo ao lado, assim: Math.random()*100. O método .floor irá pegar um número decimal e o arredonda para baixo para o número inteiro mais próximo para garantir que o número escolhido seja um número inteiro e não decimal. O método .ceil retorna numero inteiro maior ou igual ao numero decimal declarado entre parenteses.
console.log(Math.floor(Math.random() * 100));
console.log(Math.ceil(42.8));
console.log(Number.isInteger(2017.2));

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
  