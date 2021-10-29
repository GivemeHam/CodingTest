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
  a = input[1].map(Number);
  b = input[2].map(Number);

  a.sort((x, y) => {
    return x - y;
  });
  b.sort((x, y) => {
    return y - x;
  });
  let sum = 0;
  a.forEach((e, i) => {
    sum += e * b[i];
  });
  console.log(sum);

  process.exit();
});
