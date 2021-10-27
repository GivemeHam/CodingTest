// readline 모듈을 import
const readline = require("readline");

// 인터페이스 객체 생성
// process의 입출력 스트림을 input과 output에 할당
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  input = line.split(" ");
  a = parseInt(input[0].split("").reverse().join(""));
  b = parseInt(input[1].split("").reverse().join(""));

  sum = a + b;
  console.log(parseInt(sum.toString().split("").reverse().join("")));

  rl.close();
}).on("close", function () {
  process.exit();
});
