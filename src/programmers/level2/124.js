function solution(n) {
  let answer = '';
  let pow = 3**10;
  console.log(pow);
  // while(true){
  for(let ii=0; ii<11; ii++){
    if(n<=12) break;
    for(let i=3; i>0; i--){
      if(n-(pow*i) >= 0){
        console.log('ttt');
        n = n-pow*i;
        console.log(n);
        answer+=i;
        break;
      }
    }
    pow=pow/3;
    console.log('pow : ' + pow);
  }
  console.log('answer1 : ' + answer);
  console.log('n : ' + n);
  //12 under
  for(let i= 3; i>=1; i--){
    if(n-(3*i)>0){
      n = n-(3*i);
      answer += i;
    }
  }
  console.log('n2 : ' + n);

  for(let i= 3; i>=1; i--){
    if(n-i>=0){
      n = n-(3*i);
      answer += i;
    }
  }
  let answer2='';
  for(let i=0; i<answer.length; i++){
    if(answer[i]==3){
      answer2+=4;
    }
    else{
      answer2+=answer[i];
    }
  }
  return answer2;
}

const result = solution(3);
console.log(result);