# Python Dictionaries

# my_stuff = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
# print(my_stuff['key1'])             #output : value1


# my_stuff = {'key1':'value1', 'key2':'value2', 'key3':{'123':['a','b','Grab Me']}}
# print(my_stuff['key3']['123'][2])               #output :  Grab Me
#
# print(my_stuff['key3']['123'][2].upper())       #output :  GRAB ME


# my_food = { 'lunch': 'pizza', 'brkfst': 'milk'}
# print(my_food['lunch']
#
# my_food['lunch'] = 'burger'
# print(my_food['lunch'])
#
# my_food['dinner'] = 'pasta'
# print(my_food)



#Practise : refer W3 schools for more`
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict)
# print(thisdict['brand'])               #Accessing key values
# print(thisdict['model'])               #Accessing key values


# x = thisdict.get("year")           #Accessing key values using get() method
# print(x)


#Loop Through a Dictionary--
# for x in thisdict:               #print all the keys
#   print(x)

# for x in thisdict:                 #print all the values
#     print(thisdict[x])

# for x in thisdict.values():         #print all the values using values() method
#   print(x)

for x, y in thisdict.items():        #print both keys and values using items() method
    print(x, y)
