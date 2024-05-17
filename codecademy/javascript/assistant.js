//Comando Import: Um comando de importação é uma maneira de usar o código armazenado em um local diferente.
//Importar o módulo de funções de assistente de outro arquivo
//import { recordShow, setLights, setAlarm } from 'assistantFunctions';

// definying the auxiliary functions
function recordShow(startTime, endTime){
    console.log('your show will be recorded at ' + startTime + ' and will stop recording at ' + endTime);
};

function setLights(startTime, endTime){
    console.log('your lights will be turned on at ' + startTime + 'and will turned of at ' + endTime);
};

function setAlarm(startTime){
    console.log('your alarm is set to play at ' + startTime);
};

//definying the assistant functions
function myAssistant01(time, callbackFunction){
    console.log('Scheduling:');
    callbackFunction(time);
    console.log('Complete.');
};

function myAssistant02(callOtherFunction, startTime, endTime){
    console.log('hi, i am your personal assistant, how can i help you today?');
    callOtherFunction(startTime, endTime);
};

//calling the assistant functions
myAssistant01('8am', recordShow);
myAssistant01('4pm', setLights);
myAssistant01(setAlarm, '8pm');
myAssistant02(recordShow, '6pm', '8pm');
myAssistant02(setLights, '8pm', '9pm');


