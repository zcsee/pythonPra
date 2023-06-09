def twoSum(nums, target):
    hashtable = dict()
    for i, num in enumerate(nums):
        j = target - num
        if j in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []


num1 = [2, 7, 8, 9]
target1 = 9
print(twoSum(num1, target1))