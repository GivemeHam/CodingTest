function solution(x, n) {
  var answer = [];
  for(let i=1; i<=n; i++)
    answer.push(x*i);
  return answer;
}

const result = solution(2,5);
console.log(result);

/**
 * 
function solution(x, n) {
    return Array(n).fill(x).map((v, i) => (i + 1) * v)
}
 */