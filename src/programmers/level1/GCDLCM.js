//최소공배수



function solution(n, m) {
  let temp = n*m;
  var answer = [];

  n < m ? [m, n] = [n, m] : 0;

  //최소공배수
  while(true){
    let temp_n = n;
    if(n%m==0) break;
    n = m;
    m = temp_n%m;
  }
  answer.push(m);
  answer.push(temp/m);

  return answer;
}

console.log(solution(102,5));

