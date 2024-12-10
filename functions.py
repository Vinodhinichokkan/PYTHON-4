#functions

def hello_world():
    print("Hello world!")   #Hello world!
 
hello_world()

print('')
def sum(num1 ,num2):
    return num1 + num2

total = sum(70,20)
print(total)          #90

print('')

print('')

def sum(num1=0, num2=0):
    if(type(num1)is not int or type(num2)is not int):
        return 0
        return num1+ num2

total = sum()                #none
print(total)

print('')

def multiple_items(*args):
    print(args)                #('Vino', 'abi', 'hari')
    print(type(args))        #<class 'tuple'>

multiple_items("Vino","abi","hari")
 
def multi_lined_items(*args):
    print (args)           #('Chocolate', 'Ice-cream', 'Dessert')
    print(type(args))    #<class 'tuple'>

multi_lined_items("Chocolate","Ice-cream","Dessert")
















