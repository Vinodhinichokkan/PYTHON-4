nums = [3,2,78,1,5]
nums.reverse()
print(nums)  #[5, 1, 78, 2, 3]

#if we want in ascending order
nums.sort()
print(nums) #[1, 2, 3, 5, 78]

#if we want in descending order
nums.sort(reverse = True)
print(nums)  #[78, 5, 3, 2, 1]

print('')
nums = [1,24,18,5,3]
print(sorted(nums, reverse = True))
print(nums)    #[24, 18, 5, 3, 1]
                #[1, 24, 18, 5, 3]

print('')
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)  #[1, 24, 18, 5, 3]
print(mynums)  #[1, 24, 18, 5, 3]
mycopy.sort()

print(mycopy) #[1, 3, 5, 18, 24]
print(nums)  #[1, 24, 18, 5, 3]


