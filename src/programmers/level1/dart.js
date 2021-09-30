function solution(dartResult) {
  let answer = 0;
  let score = 0;
  let bonus = 0;
  let option = '';
  let option2 = '';
  for(let i =dartResult.length; i>=0 ; i--){

    //option
    if((/[*#]/).test(dartResult[i])){
        
      if(dartResult[i] == '*'){
        option = '*';
      }
      else {
        option = '#';
      }
    }

    //bonus
    if((/[SDT]/).test(dartResult[i])){
      if(dartResult[i] === 'S')
        bonus = 1;
      if(dartResult[i] === 'D')
        bonus = 2;
      if(dartResult[i] === 'T')
        bonus = 3;      
    }
  

    //숫자일경우
    if(!(/[^0-9]/).test(dartResult[i])){
      score = dartResult[i];
      if(dartResult[i] == 0 && dartResult[i-1] == 1 ){
        score = 10;
        i--;
      }

      score = Number(score);
      //score
      if(option == '*'){
        score = Math.pow(score, bonus) * 2;
      }
      if(option == '#'){
        score = Math.pow(score, bonus) * -1;
      }
      if(option == ''){
        score = Math.pow(score, bonus);
      }
      if(option2 == '*'){
        score *= 2;
        option2 = '';
      }
      answer += score;
      if(option =='*') option2 = '*';

      option = '';
      score = 0;
    }
    
  }
  
  return answer;
}

const result = solution('1D2S0T');

console.log(result);



/**
 * function solution(dartResult) {
    const bonus = { 'S': 1, 'D': 2, 'T': 3 },
          options = { '*': 2, '#': -1, undefined: 1 };

    let darts = dartResult.match(/\d.?\D/g);

    for (let i = 0; i < darts.length; i++) {
        let split = darts[i].match(/(^\d{1,})(S|D|T)(\*|#)?/),
            score = Math.pow(split[1], bonus[split[2]]) * options[split[3]];

        if (split[3] === '*' && darts[i - 1]) darts[i - 1] *= options['*'];

        darts[i] = score;
    }

    return darts.reduce((a, b) => a + b);
}

 */