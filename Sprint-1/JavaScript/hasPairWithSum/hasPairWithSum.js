/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O( n^2)
 * Space Complexity:O(1)
 * Optimal Time Complexity: O(n)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i] + numbers[j] === target) {
        return true;
      }
    }
  }
  return false;
}

// Since function is to loop inside another loop, it is roughly n × n comparisons, so 
// time complexity = O(n²)
// Because we do not create another array, object or set that grows with n, space 
// complexity should be O(1)
// Optimal means the best complexity we can achieve with a reasonable algorithm for the problem.
// We can use a Set to remember numbers we've already seen for this function.
export function hasPairWithSum(numbers, target) {
  const seen = new Set();

  for (const number of numbers) {
    const needed = target - number;

    if (seen.has(needed)) {
      return true;
    }

    seen.add(number);
  }

  return false;
} 
// Instead of checking every possible pair, we ask:
// "Have I already seen the number that would make this number equal the target?"
// which makes optimal time complexity O(n)
