const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  solution();
  process.exit();
});
function solution() {
  let n = parseInt(input[0].split(" ")[0]);
  let m = parseInt(input[0].split(" ")[1]);

  let know = input[1].split(" ").map(Number);

  if (know.shift() == 0) {
    console.log(m);
  } else {
    let party = [];
    for (let i = 2; i < 2 + m; i++) {
      temp = input[i].split(" ").map(Number);
      temp.shift();
      party.push(temp);
    }

    let queue = know;
    let knows = new Array(50).fill(0);
    cnt = 0;

    while (queue.length > 0) {
      q = queue.shift();
      knows[q] = 1;
      for (let j = 0; j < m; j++) {
        if (party[j].indexOf(q) != -1) {
          party[j].forEach((e) => {
            if (knows[e] == 0) queue.push(e);
            knows[e] = 1;
          });
          party[j] = [];
          cnt += 1;
        }
      }
    }
    console.log(m - cnt);
  }
}
