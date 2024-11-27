#tuples are immutable which cannot be changed

mytuple = tuple(('vino',42,True))

anothertuple = (1,4,2,8,2,2)

print(mytuple)   #('vino', 42, True)
print(type(mytuple))   #<class 'tuple'>
print(type(anothertuple))   #<class 'tuple'>

print('')
newlist = list(mytuple)
newlist.append('Abi')
newtuple = tuple(newlist)
print(newtuple)  #('vino', 42, True, 'Abi')

print('')
(one, *two, hey) = anothertuple
print(one)    #1
print(two)    #[4,2,8,2]
print(hey)    #2

print(anothertuple.count(2))  # 3  -->it will give how many times 2 is there in the list

