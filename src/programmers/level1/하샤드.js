function fun(sum, x){
  console.log(sum,x);

  if(x < 10) {
    return sum+x;
  }
  return fun(sum+x%10, parseInt(x/10)) ;
}
function solution(x) { 
  if(x % fun(0, x) == 0) return true;
  else return false;
}

console.log('answer : ' + solution(10));


/*
function Harshad(n){
  return !(n % (n + "").split("").reduce((a, b) => +b + +a ));
}
*/