const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  n = input.shift();
  input = new Set(input);
  input = [...input];
  console.log(input);
  input.sort((a, b) => {
    if (a.length > b.length) return 1;
    if (a.length < b.length) return -1;
    if (a > b) return 1;
    if (a < b) return -1;
    return 0;
  });
  console.log(input);
  input.map((e) => console.log(e));
  process.exit();
});
