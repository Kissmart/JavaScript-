let nestedArray = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

function calculateTotal(nestedArray) {
  let total = 0;
  
  for (let i = 0; i < nestedArray.length; i++) {
    for (let j = 0; j < nestedArray[i].length; j++) {
      total += nestedArray[i][j];
    }
  }
  
  return total;
}

let totalSum = calculateTotal(nestedArray);
console.log("Total sum:", totalSum);
