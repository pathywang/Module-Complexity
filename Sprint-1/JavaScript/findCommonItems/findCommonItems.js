/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(nm)
 * Space Complexity:O(n+m)
 * Optimal Time Complexity: 0(n+m)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => [
  ...new Set(firstArray.filter((item) => secondArray.includes(item))),
];

// Suppose that firstArray has n items and secondArray has m items.
// filter() goes through every item in firstArray → O(n) iterations.
// includes() may have to search through the entire secondArray → O(m).
// so n items × m-item search = O(nm) for time complexity
// Due to that the array produced by filter() and the final array created 
// by [...new Set(...)]. These all can grow with input size. So space complexity is O(n+m)
// However,we don't necessarily need to search through secondArray from scratch for every 
// item. We could turn secondArray into a Set first:
// export const findCommonItems = (firstArray, secondArray) => {
//    const secondSet = new Set(secondArray);
//     return [...new Set(
//              firstArray.filter(item => secondSet.has(item))
//     )];
//   }; which would create Set: O(m) and search n items: O(n) so total size: O(n + m)
