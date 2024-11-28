#sets

#No duplicates allowed

#you cannot refer to an element in the set with an index position or a key

nums = {1,2,3,4}

nums2 = set((1,2,3,4))

print(nums)  #{1,2,3,4}
print(nums2) #{1,2,3,4}
print(type(nums)) #<class 'set>
print(len(nums))  #4

print('')

nums ={1,2,2,3}
print(nums)  #{1,2,3} --->because duplictes were not allowed.

#true is a dupe of 1,False is a dupe of zero

print('')
nums ={1,True,2,False,3,4,0}
print(nums)   #{False, 1, 2, 3, 4}

#add elements from one set to another

morenums = {5,6,7}
nums.update(morenums)
print(nums)  #{False, 1, 2, 3, 4, 5, 6, 7}

#you can use update with lists,tuples and dictionaries too..
 
 #merge two sets to create a new set

one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)  #{1, 2, 3, 5, 6, 7}

#keep only the duplicates

one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)  #{2,3}

# keep everything except the duplicates

one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)  #{1,4}




