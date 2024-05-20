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
  