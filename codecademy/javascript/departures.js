/*Objetivo: Filtrar departures para obter os horários antes e após o meio-dia e armazená-los em eveningTimes e morningTimes. Passo a passo da solução:
Departures é uma array de strings, cada string é um número seguido de 'am' ou 'pm'.
As funções morning e evening são criadas e recebem um argumento (array), depois, em seus blocos {}, rodam o método .includes(), que percorre cada item da lista e verifica se contém 'am' e 'pm' como valor, retornando true e/ou false.
O método .filter() aplica um teste a cada elemento em uma array e retorna uma nova array que contém apenas os elementos que retornam true.
As variáveis morningTimes e eveningTimes são criadas para armazenar separadamente os horários da manhã e da noite contidos na array departures, para tanto, chamam a variável departure e aplicam os métodos que se seguem.
Quando o método .filter() é aplicado a departures e usa como argumento as funções criadas, elas rodam o .include() na array e classificam quais elementos são true e false, na sequencia, o .filter() pode então filtrar apenas os elementos classificados como true, pois, se a verificação for falsa, não passa no filtro.
Quando o console loga morningTimes, somente os elementos que incluam 'am' são impressos, o mesmo ocorre com eveningTimes, imprimindo apenas itens com 'pm'*/

let departures = [
    '8pm',
    '9pm',
    '10pm',
    '11pm',
    '8am',
    '9am',
    '10am',
    '11am',
  ];
  function morning(array){
    return array.includes('am');
  };
  function evening(array){
    return array.includes('pm');
  };
  let morningTimes = departures.filter(morning);
  let eveningTimes = departures.filter(evening);
  console.log(morningTimes);
  console.log(eveningTimes);
  