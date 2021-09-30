function solution(phone_number) {
  let answer = '';
  answer = phone_number.slice(-4);
  
  return answer.padStart(phone_number.length, '*');
}

console.log(solution('01084561183'));