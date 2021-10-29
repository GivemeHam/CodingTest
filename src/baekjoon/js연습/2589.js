const { SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION } = require("constants");
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let matrix = [];
let answer = -1;
dx = [0, 0, 1, -1];
dy = [1, -1, 0, 0];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  solution(input);

  process.exit();
});
function solution(inputs) {
  y = parseInt(input[0].split(" ")[0]);
  x = parseInt(input[0].split(" ")[1]);
  for (let i = 1; i <= y; i++) {
    matrix.push(input[i].split(""));
  }
  let maxValue = 0;
  for (let i = 0; i < y; i++) {
    for (let j = 0; j < x; j++) {
      if (matrix[i][j] == "L") {
        value = bfs([i, j]);
        if (value > maxValue) {
          maxValue = value;
        }
      }
    }
  }
  console.log(maxValue);

  function bfs(start) {
    let queue = [start];
    let weight = [0];
    let visit = [];

    for (let i = 0; i < y; i++) {
      line = [];
      for (let j = 0; j < x; j++) {
        line.push(0);
      }
      visit.push(line);
    }
    visit[start[0]][start[1]] = 1;

    maxW = 0;
    while (queue.length > 0) {
      q = queue.shift();
      w = weight.shift();

      maxW = Math.max(w, maxW);

      for (let k = 0; k < 4; k++) {
        let yy = q[0] + dy[k];
        let xx = q[1] + dx[k];
        if (xx >= 0 && xx < x && yy >= 0 && yy < y && matrix[yy][xx] == "L") {
          if (visit[yy][xx] == 0) {
            queue.push([yy, xx]);
            weight.push(w + 1);
            visit[yy][xx] = 1;
          }
        }
      }
    }
    return maxW;
  }
}
