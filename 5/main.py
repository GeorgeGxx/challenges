""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may not use the same element twice. """



Input: nums = [6,3,5,7], target = 9
Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].





Input: nums = [3,2,4], target = 6
Output: [1,2]





Input: nums = [3,3], target = 6
Output: [0,1]



#*Not consecutive
Input: nums = [2,3,4], target = 6
Output: [0,2]



#*Not consecutive, more than 2 digits
Input: nums = [9,9,2,9,3,9,9,4], target = 6
Output: [2,7]



#*More than 2 indexes
Input: nums = [9,9,2,9,3,9,9,2], target = 7
Output: [2,4,7]