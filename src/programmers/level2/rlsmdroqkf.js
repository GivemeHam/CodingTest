function solution(progresses, speeds) {
  let answer = [];
  let n = progresses.length;
  let work = 0;

  while(true){
    if(work>=n) break;
    for(let i=0; i<n; i++){
      progresses[i]+=speeds[i];
    }
    // console.log(progresses);
    if(progresses[work]>=100){
      let k=1;
      for(let j=work+1; j<n; j++){
        if(progresses[j]>=100){
          k++;
        }
        else{
          break;
        }
      }
      work+=k;
      answer.push(k);
    }
  }
  return answer;
}

const result = solution([93, 30, 55], [1, 30, 5]);

console.log(result);

// function solution(progresses, speeds) {
//   let answer = [0];
//   let days = progresses.map((progress, index) => Math.ceil((100 - progress) / speeds[index]));
//   let maxDay = days[0];

//   for(let i = 0, j = 0; i< days.length; i++){
//       if(days[i] <= maxDay) {
//           answer[j] += 1;
//       } else {
//           maxDay = days[i];
//           answer[++j] = 1;
//       }
//   }

//   return answer;
// }