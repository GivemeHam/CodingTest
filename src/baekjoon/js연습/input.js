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
  input[1].map(Number);
  console.log(input);

  process.exit();
});
