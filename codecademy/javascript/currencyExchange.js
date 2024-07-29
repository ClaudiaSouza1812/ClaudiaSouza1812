//declarações de funções
function inYen(dollar){
    let amount = dollar * 113;
      return amount;
  };
    console.log('the exchanged amount is ' + inYen(100));
  
  //declarações de funções: nesta declaração, determinamos que o valor inserido em wallet, em seguida, criamos uma função chamada exchangeToReal, ela  possui um argumento que determina que o valor que está dando entrada é em dollar, por isso se chama dollar. Na sequência, criamos a fórmula que esta declaração rodará, nela declaramos uma varivel do tipo "let" com o nome da moeda a ser cambiada, que retornará o valor do dólar vezes o valor equivalente a moeda, então saberemos que toda vez que a função exchangeToReal for chamada, será feito o cambio de dollar para real.
  let wallet = 1000;
  function exchangeToReal01 (dollar) {
    let real = dollar * 5.42;
     return real;
  };
  function exchangeToReal02 (euro) {
    let real = euro * 5.45;
    return real;
  };
  function exchangeToDollar (real){
    let dollar = real / 5.42;
    return dollar;
  };
  function exchangeToEuro (real){
    let euro = real / 5.45;
    return euro;
  };
  console.log('the amount of ' + wallet + ' dollares exchanged to Real is ' + exchangeToReal01(wallet) + ' reais');
  console.log('the amount of ' + wallet + ' euros exchanged to Real is ' + exchangeToReal02(wallet) + ' reais');
  console.log('the amount of ' + wallet + ' reais exchanged to Dollar is ' + exchangeToDollar(wallet) + ' dolares');
  console.log('the amount of ' + wallet + ' reais exchanged to Euro is ' + exchangeToEuro(wallet) + ' euros');
  