const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  l = line.split(" ");
  input.push(l);
}).on("close", function () {
  n = parseInt(input[0][0]);
  score = parseInt(input[0][1]);
  p = parseInt(input[0][2]);
  scoreList = input[1];
  if (n == 0) {
    console.log(1);
  } else {
    if (n == p && scoreList[n - 1] >= score) {
      console.log(-1);
    } else {
      res = n + 1;
      for (let i = 0; i < n; i++) {
        if (scoreList[i] <= score) {
          res = i + 1;
          break;
        }
      }
      if (res > p) {
        console.log(-1);
      } else {
        console.log(res);
      }
    }
  }

  process.exit();
});
