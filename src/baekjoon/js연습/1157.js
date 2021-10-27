// readline 모듈을 import
const readline = require("readline");

// 인터페이스 객체 생성
// process의 입출력 스트림을 input과 output에 할당
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  input = line.toUpperCase().split("");
  arr = new Array(26).fill(0);

  for (let i = 0; i < input.length; i++) {
    ascii = input[i].charCodeAt(0);
    arr[ascii - 65]++;
  }
  maxN = Math.max(...arr);
  cnt = 0;
  for (let i = 0; i < 26; i++) {
    if (maxN == arr[i]) {
      cnt++;
    }
  }
  if (cnt > 1) {
    console.log("?");
  } else {
    console.log(arr.indexOf(maxN));
    console.log(String.fromCharCode(arr.indexOf(maxN) + 65));
  }
  rl.close();
}).on("close", function () {
  process.exit();
});
