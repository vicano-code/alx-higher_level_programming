#!/usr/bin/node

function secondBiggestNum (argList) {
  const argSize = argList.length;
  // check if aany argument was supplied
  if (argSize <= 3) {
    console.log(0);
  } else {
    for (let i = 2; i < argSize; i++) {
      let num = 0; // num-number of values a number is greater than
      for (let j = 2; j < argSize; j++) {
        if (parseInt(argList[i]) > parseInt(argList[j])) {
          num++;
        }
      }
      /* 2 subtracted twice: first two values account for non argument elem
       * in argv list while the other 2 accounts for the biggest value &
       * the secon biggest vaue itself
       */
      if (num === argSize - 2 - 2) {
        console.log(argList[i]);
        return;
      }
    }
  }
}
// Call the function
secondBiggestNum(process.argv);
