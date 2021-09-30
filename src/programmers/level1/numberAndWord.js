// function solution(s) {
//   let wordToNum = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
//   let answer = '';
//   for(let i=0; i<s.length; i++){

//     //not Number
//     if((/[^0-9]/).test(s[i])){
      
//       //word check
//       for(let j=i; j<=s.length; j++){
//         let tempWord = s.substr(i,j-i);
//         if(wordToNum.indexOf(tempWord)!=-1){
//           answer+=wordToNum.indexOf(tempWord);
//           //  i=i+j;
//           break;
//         }
//       }
//     }
//     else{
//       answer+=s[i];
//     }
//   }
//   return Number(answer);
// }

const result = solution('2three45sixseven');

console.log(result);



function solution(s) {
  let numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
  var answer = s;

  for(let i=0; i< numbers.length; i++) {
      let arr = answer.split(numbers[i]);
      console.log(arr);
      answer = arr.join(i);
  }

  return Number(answer);
}