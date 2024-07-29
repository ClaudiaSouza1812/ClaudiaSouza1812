
//function declaration can be made without parameter:
function greetWorld(){
    console.log('Hello, World!');
  }
  console.log(greetWorld());
  
  //function declaration also can be made with one, two or more parameters:
  function calculateArea(width, height){
    console.log(width * height);
  }
  console.log(calculateArea(2,2));
  
  //function expression can be made with or without parameters, this one has two:
  const calculateArea1 = function(width, height){
    const area = width * height;
    return area;
  }
  console.log(calculateArea1(4,4));
  
  //Arrow function notation can be made with or without parameters, this one has two:
  const calculateArea2 = (width, height) => {
    const area = width * height;
    return area;
  }
  console.log(calculateArea2(5,5));
  
  //concise arrow notation: The parentheses can be removed, since it has a single parameter. The curly braces { } can be removed since the function consists of a single-line block. The return keyword can be removed since the function consists of a single-line block.
  const sumNumbers = number => number + number;
  console.log(sumNumbers(10)); 

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