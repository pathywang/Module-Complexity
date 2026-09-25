/**
 * Calculate the sum and product of integers in a list
 *
 * Note: the "sum" is every number added together
 * and the "product" is every number multiplied together
 * so for example: [2, 3, 5] would return
 * {
 *   "sum": 10, // 2 + 3 + 5
 *   "product": 30 // 2 * 3 * 5
 * }
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  for (const num of numbers) {
    sum += num;
  }

  let product = 1;
  for (const num of numbers) {
    product *= num;
  }

  return {
    sum: sum,
    product: product,
  };
}

// For two loops, we have visit each element of array  in order to get the result
// so time complexity is O (n) which means linear. 
// Regarding space complexity, we only get one result
// for sum and product no matter how long the array is.so it is O(1)(constant)
// While time complexity is O(n), optimal time complexity should be O(n) because loop 
// has to go each single element in array.
