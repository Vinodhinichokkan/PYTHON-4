def add(*num):
    sum = 0
    for n in num:
        sum = sum + n

    print("Sum:", sum)          #8

add(2,6)

print('')

def multi_named_items(**Kwargs):
    print(Kwargs)              #{'first': 'Subscribe', 'last': 'share'}
    print(type(Kwargs))    #<class 'dict'>

multi_named_items(first="Subscribe",last="share")


print('')

def func(a,b,*args, option =False,**Kwargs):
    print(a,b)            #1 3
    print(args)            #(10,20)
    print(option)        #False
    print(Kwargs)        #{'Name': 'Vino', 'Salary': 60000}

func(1,3,10,20,Name = 'Vino', Salary = 60000)







