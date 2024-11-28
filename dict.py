#dictionaries

#keys should be unique in dict 

car ={
    "brand": "Tesla",
    "model": "Model_3_P",
    "year": 2024
}

car2 = dict(brand="Tesla",
            model="Model_3_P")

print(car)   #{'brand': 'Tesla', 'model': 'Model_3_P', 'year': 2024}
print(car2)  #{'brand': 'Tesla', 'model': 'Model_3_P'}
print(type(car))  #<class 'dict'>
print(len(car))  #3

#Access items
print('')

print(car["brand"])  #Tesla
print(car.get("model"))  #Model_3_P

#list all keys
print(car.keys()) #dict_keys(['brand', 'model', 'year'])

#list all values
print(car.values())  #dict_values(['Tesla', 'Model_3_P', 2024])

#list all key/value pairs as tuples
print(car.items())   #dict_items([('brand', 'Tesla'), ('model', 'Model_3_P'), ('year', 2024)])

#verify a key exists or not

print("model" in car)  #True
print("price" in car)  #False

#change values
car["brand"] = "Nio"
car.update({"price": 10000})

print('')
print(car)  #{'brand': 'Nio', 'model': 'Model_3_P', 'year': 2024, 'price': 10000}

print('')
#remove items
print(car.pop("price"))
print (car)   #{'brand': 'Nio', 'model': 'Model_3_P', 'year': 2024}

print('')
print(car.popitem())  #('year', 2024)
print(car)    #{'brand': 'Nio', 'model': 'Model_3_P'}

#delete and clear
car["EV"] = "Yes"
del car["EV"]
print(car)    #{'brand': 'Nio', 'model': 'Model_3_P'} 

car2.clear()
print(car2)  #{}

del car2

#copy dictionaries
print('')
car2 = car.copy()
car2["EV"] = "NO"

print("Good copy!")  #Good copy!
print(car)    #{'brand': 'Nio', 'model': 'Model_3_P'}
print(car2)  #{'brand': 'Nio', 'model': 'Model_3_P', 'EV': 'NO'}

#use the dict()constructor function

car3 = dict(car)
print('')

print("Good copy!")   #Good copy!
print(car3)  #{'brand': 'Nio', 'model': 'Model_3_P'}

#nested dictionaries

member1 ={
    "name": "Vino",
    "instrument": "brand"
}
member2 ={
    "name": "Abi",
    "instrument": "model"
}
band = {
    "member1" : member1,
    "member2" : member2
}
print('')
print(band)  #{'member1': {'name': 'Vino', 'instrument': 'brand'}, 'member2': {'name': 'Abi', 'instrument': 'model'}}







