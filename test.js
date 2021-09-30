function solution(id_list, report, k) {
  let reportCount = [];
  let answerA = [];
  //delete dupl
  report = report.filter((element, index) => {
    return report.indexOf(element) === index;
  });
  //answer init
  for (let i = 0; i < id_list.length; i++) {
    answerA.push(0);
    reportCount.push(0);
  }

  //reportCount
  report.forEach((e) => {
    temp = e.split(" ")[1];
    reportCount[id_list.indexOf(temp)]++;
  });

  //
  for (let i = 0; i < id_list.length; i++) {
    if (reportCount[i] >= k) {
      report.forEach((e) => {
        temp = e.split(" ");
        if (id_list[i] == temp[1]) {
          answerA[id_list.indexOf(temp[0])]++;
        }
      });
      id_list[i]; //frodo
    }
  }

  console.log(answerA);

  return answerA;
}

let result = solution(
  ["muzi", "frodo", "apeach", "neo"],
  ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
  2
);
