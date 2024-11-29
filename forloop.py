#for loop
fruits = ["apple","banana","orange"]
for x in fruits:
    print(x)

#apple
#banana
#orange
print('')

fruits = ["apple","banana","orange"]
for x in fruits:             
    if x == "banana":
        break
    print(x)          #apple

for x in "share":  #s
    print(x)       #h
                   #a
                   #r
                   #e
for x in range(10): # 0 1 2 3 4 5 6 7 8 9
    print(x)

for x in range(2,4):
    print(x)          #2 3

for x in range(0,101,5):
    print(x)  #o/p will be 0 5 10 15 20 25 30 35 40......

print('')

names = ["vino","abi","hari"]
actions = ["codes","eats","sleeps"]

for name in names: 
                    
 for action in actions:
        print(name + " " + action + ".")   #vino codes.
                                           # vino eats.
                                           #vino sleeps.
                                           #abi codes.
                                           #abi eats.
                                           #abi sleeps.
                                           #hari codes.
                                           #hari eats.
                                           #hari sleeps.
for name in names: 
                    
 for action in actions:
        print(name + " " + action + ".") 







