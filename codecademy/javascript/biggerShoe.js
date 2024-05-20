
//in this code, we will make a function that receives two arguments, they are numbers os shoes. This function run an if else and else if statements that checks wich user have the bigger shoe or if both have the same number of a shoe. The console.log will be called an will receive the function as argument, which in turn will receive the variables declared that contains the shoe numbers as its argument, printing the result.
let izaShoe = 39;
let luizaShoe = 39;

function shoesSizesComparation(sizeIza, sizeLuiza) {
  if(sizeIza > sizeLuiza) {
    console.log(`Iza\`s wear a ${izaShoe} shoe number, bigger then Luiza\`s shoe.`);
  } else if(sizeLuiza > sizeIza) {
    console.log(`Luiza\`s wear a ${luizaShoe} shoe number, bigger then Iza\`s shoe.`);
  } else if(sizeIza === sizeLuiza) {
    console.log(`Iza e Luiza wear the same shoe number`);
  } else {
    console.log(`you can only type numbers, check your information`);
  }
}
console.log(shoesSizesComparation(izaShoe, luizaShoe));