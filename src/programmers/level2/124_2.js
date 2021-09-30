function calc(n) {
  let answer = String(n%3).replace(0,4);
  console.log(answer);

  if(parseInt((n-1)/3)<=0){
    return answer;
  }
  return calc(parseInt((n-1)/3)) + answer;
}

function solution(n) {
  return calc(n);
}

const result = solution(10);
console.log(result);