function solution(n, arr1, arr2) {
  let answer = [];
  let arr = [];
  for(let i = 0; i<n; i++){
    //padStart
    arr.push((arr1[i]|arr2[i]).toString(2).padStart(n,0));
  }
  
  for(let i=0; i<n; i++){
    let temp = '';
    for(let j=0; j<n; j++){
      
      if(arr[i][j]==1){
        temp+='#'
      }
      else{
        temp+=' ';
      }
    }
    answer.push(temp);
  }
  return answer;
}

const result = solution(	6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]);
console.log(result);


// function solution(n, arr1, arr2) {
//     return arr1.map((v, i) => addZero(n, (v | arr2[i]).toString(2)).replace(/1|0/g, a => +a ? '#' : ' '));
// }

// const addZero = (n, s) => {
//     return '0'.repeat(n - s.length) + s;
// }
