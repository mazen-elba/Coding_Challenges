def twoNumbersSum(array, targetSum):
    # 1. O(N^2) time | O(1) space
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if targetSum == firstNum + secondNum:
                return [firstNum, secondNum]
    return []

    # # 2. O(N) time | O(N) space
    # numbers = {}
    # for num in array:
    #     potentialMatch = targetSum - num
    #     if potentialMatch in numbers:
    #         return [potentialMatch, num]
    #     else:
    #         numbers[num] = True
    # return []

    # # 3. O(Nlog(N)) time | O(1) space
    # array.sort()
    # left = 0
    # right = len(array) - 1
    # while left < right:
    #     currentSum = array[left] + array[right]
    #     if currentSum == targetSum:
    #         return [array[left], array[right]]
    #     elif currentSum > targetSum:
    #         right -= 1
    #     elif currentSum < targetSum:
    #         left += 1
    # return []


# --- Driver Method to Test Cases --- #
print(twoNumbersSum([4, 6], 10))  # => [4, 6]
print(twoNumbersSum([4, 6, 1], 5))  # => [4, 1]
print(twoNumbersSum([4, 6, 1, -3], 3))  # => [6, -3]
print(twoNumbersSum([3, 5, -4, 8, 11, 1, -1, 6], 10))  # => [11, -1]
print(twoNumbersSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))  # => [8, 9]
print(twoNumbersSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))  # => [3, 15]
print(twoNumbersSum([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5))  # => [-5, 0]
# => [210, -47]
print(twoNumbersSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163))
print(twoNumbersSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164))  # => []
print(twoNumbersSum([3, 5, -4, 8, 11, 1, -1, 6], 15))  # => []
