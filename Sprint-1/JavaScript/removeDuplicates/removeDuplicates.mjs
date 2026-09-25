/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n^2)
 * Space Complexity:O(n)
 * Optimal Time Complexity:O(n)
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const uniqueItems = [];

  for (
    let currentIndex = 0;
    currentIndex < inputSequence.length;
    currentIndex++
  ) {
    let isDuplicate = false;
    for (
      let compareIndex = 0;
      compareIndex < uniqueItems.length;
      compareIndex++
    ) {
      if (inputSequence[currentIndex] === uniqueItems[compareIndex]) {
        isDuplicate = true;
        break;
      }
    }
    if (!isDuplicate) {
      uniqueItems.push(inputSequence[currentIndex]);
    }
  }

  return uniqueItems;
}

// While function shows loop inside another loop(nested loop), time complexity is O(n^2)
// Because  uniqueItems is extra storage, space complexity is O(n)
// Again, we can use Set to make another function which makes faster to run
export function removeDuplicates(inputSequence) {
  return [...new Set(inputSequence)];
}
// So optimal time complexity should be O(n)
