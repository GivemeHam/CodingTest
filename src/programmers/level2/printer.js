function solution(priorities, location) {
  var answer = 0;
  let value = priorities[location];
  let pr = priorities.map((e,i) => {
    return {e, index:i};
  });

  pr = pr.sort((a,b) => { 
    if(a.e)
    return b.e-a.e;
  });
  console.log(pr);
  const found = pr.findIndex(elem => elem.e===value);

  let start =pr[found-1].index;
  console.log(pr[found-1].index);

  let pr3 = []
  let pr2 = pr.find(elem => {
    return elem.e === value && elem.index>start
  });
  pr3.push(pr2);
  console.log(pr2);

  console.log(found);
  return answer;
}

const result = solution([2, 1, 9, 1, 2, 1,1],1);
// console.log(result);