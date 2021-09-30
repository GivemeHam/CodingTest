function solution(dartResult) {
  var answer = 0;
  let stack = [];
  let arr = dartResult.split('');
  let scoreArr = [];
  let turn = -1;
  arr.map((data, i)=>{
      //10 일때 따로 빼야됨
      if(!isNaN(parseInt(data)) && arr[i-1] != '1') {

        if((parseInt(data))===1 && arr[i+1] ==0){
          stack.push(10);
        }
        else{
          stack.push(parseInt(data));
        }
        turn++;
      }
      if(data==='S'){
          let score = stack.pop();
          scoreArr.push(score);
      }
      if(data==='D'){
          let score = stack.pop();
          scoreArr.push(score*score);
      }
      if(data==='T'){
          let score = stack.pop();
          scoreArr.push(score*score*score);
      }
      
      if(data==='*'){
          scoreArr[turn]=scoreArr[turn]*2;
        //flag 같은거 없어도 됨 요 아랫줄이 다 처리해줌
          scoreArr[turn-1]=scoreArr[turn-1]*2;  
      }

      if(data==='#'){
          scoreArr[turn]=scoreArr[turn]*-1;
      }
      
  })
  scoreArr.map(data=>{
      answer+=data;
  })
  return answer;
}


const result = solution('1D2S0T');

console.log(result);