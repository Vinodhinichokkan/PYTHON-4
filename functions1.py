def add(*num):
    sum = 0
    for n in num:
        sum = sum + n

    print("Sum:", sum)          #8

add(2,6)

print('')

def multi_named_items(**Kwargs):
    print(Kwargs)
    print(type(Kwargs))

multi_named_items("Subscribe","share")








