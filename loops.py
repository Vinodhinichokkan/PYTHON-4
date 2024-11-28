#while loop

i=1
while i<6:
    print(i)
    i+= 1   

#1
#2
#3
#4
#5


i=1
while i<6:
    print(i)
    if i == 3:
        break
    i+= 1  
#1
#2
#3 
print('')
i=1
while i<10:
    i+= 1
    if i == 3:
        continue
    print(i)
else:
    print("i is no longer less than 10")

#2
#4
#5
#6
#7
#8
#9
#10