# LIST ["item", "item","item" ]
# Tuple ("item", "item","item" )
# Set {"item", "item","item" }
# Dictionary {"key":"value", "key":"value", "key":"value"}

# List is used to store multiple items in a single variable

#List Items :
    # Ordered
        # (when we add new item to the list, 
        # the order wont change, and the added item will
        # be placed at the end of the list)
    # Changeable
        # (we can change, add, & remove items in a list 
        # after it has been created)
    # Allow duplicates
        # ( since list is indexed, list can have items with
        # the same value)



# create a list
thislist=["apple", "banana", "strawberry"]
print(thislist)
# ['apple', 'banana', 'strawberry']

# list length
print(len(thislist))
# 3

# data types
# list items can be of any data type
list1 = ["apple", "banana", "ananas"] # string
list2 = [1,2,4,5,7,6,9,3] # int
list3 = [True, False, True] # boolean
list4 = ["abcd", 123, True, "efg", 60] # mix

# type()
# From Python's perspective, lists are defined 
# as objects with the data type 'list'
mylist = [True, True, False]
print(type(mylist))
# <class 'list'>

# list() constructor
# It is also possible to use the list() constructor
#  when creating a new list

thislist1 = list(("apple","banana","coconut"))
print(thislist1)
# ['apple', 'banana', 'coconut']






#----------------- Access List Items---------------------
# List items are indexed, we can access them 
# by referring to the index number:

thislist2 = ["laptop", "mouse", "monitor"]
print(thislist2[1])
# mouse

print(thislist2[-1]) #from backward
# monitor


thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[2:5]) # return the third, fourth, & fifth items
# ['cherry', 'orange', 'kiwi']

print(thislist3[:3]) #from the beginning
# ['apple', 'banana', 'cherry']

print(thislist3[4:])
# ['kiwi', 'melon', 'mango']

print(thislist3[-4:-1])
# ['orange', 'kiwi', 'melon']



# ____Check if item exists___
if "coconut" in thislist3:
  print("Yes, 'apple' is in the fruits list")
else:
  print("This fruit is not in the list")

# This fruit is not in the list






#------------------ Change List Items ------------------

thislist4 = ["socks", "pants", "t-shirt", "jeans", "hat", "jacket"]

thislist4[1] = "rock"
print(thislist4)
# ['socks', 'rock', 't-shirt', 'jeans', 'hat', 'jacket']

thislist4[1:3]=["sweater","panty"]
print(thislist4)
# ['socks', 'sweater', 'panty', 'jeans', 'hat', 'jacket']

# If you insert more/less items than you replace, the new items
# will be inserted where you specified, and the remaining
# items will move accordingly


#____ insert() ____

thislist5 = ["a", "e", "i"]
thislist5.insert(2,"u") # this will go to index #2
print(thislist5)
# ['a', 'e', 'u', 'i']






#-----------------  Add List Items  -------------------

# append()
colors = ["red", "black", "green"]
colors.append("orange")
print(colors)
#['red', 'black', 'green', 'orange']

# insert()
colors.insert(1,"blue")
print(colors)
#['red', 'blue', 'black', 'green', 'orange']

# extend
dark = ["grey, brown, coal"]
colors.extend(dark)
print(colors)
# ['red', 'blue', 'black', 'green', 'orange', 'grey, brown, coal']

# add any iterable
a_tuple = ("pink", "babyblue")
colors.extend(a_tuple)
print(colors)
#['red', 'blue', 'black', 'green', 'orange', 'grey, brown, coal', 'pink', 'babyblue']






#----------------  Remove List Items  -----------------

# remove()
colors.remove("black")
colors.remove("red")
colors.remove("blue")
print(colors)
# ['green', 'orange', 'grey, brown, coal', 'pink', 'babyblue']

# pop()
colors.pop(1) #remove specified index
print(colors)
#['green', 'grey, brown, coal', 'pink', 'babyblue']

colors.pop() #if not specified it will remove the last item
print(colors)
# ['green', 'grey, brown, coal', 'pink']


# del
del colors[0]
print(colors)
#['grey, brown, coal', 'pink']

# clear()
colors.clear()
print(colors)
# []  #the list remain, but has no content

del colors #this will delete the entire list





#------------------  Loop Lists  ----------------------

lands = ["DE", "UK", "NE", "SP"]

# print all the items in the list, one by one
for land in lands:
   print(land)

# DE
# UK
# NE
# SP

# Print all items by referring to their index number
for i in range(len(lands)):
  print(i, lands[i])

# 0 DE
# 1 UK
# 2 NE
# 3 SP

# Print all items, using a while loop to go
#  through all the index numbers
subjects = ["maths","biology","physics"]
i = 0
while i< len(subjects):
  print(i, subjects[i])
  i += 1

# 0 maths
# 1 biology
# 2 physics

# using list comprehension
[print(x) for x in subjects]

# maths
# biology
# physics




#----------------  List Comprehension  ----------------

humans = ["understanding_human", "immoral_human", "destructive_human", "overcompetitive_human", "real_human", "growthmindset_human"]
my_environment=[]

for human in humans:
  if "growth" in human:
    my_environment.append(human)
  elif "understanding" in human:
    my_environment.append(human)
  elif "real" in human:
    my_environment.append(human)

print("I grow well when i am surrounded by:", ','.join(my_environment))
# I grow well when i am surrounded by: understanding_human,real_human,growthmindset_human



# with list comprehension

kitchen = ["spoon", "fork", "knife", "ladle"]
newlist = [x for x in kitchen if "o" in x]
print(newlist)
# ['spoon', 'fork']

# the Syntax
# newlist = [expression for item in iterable if condition == True]

newlist = [x for x in kitchen if x != "fork"]
print(newlist)
# ['spoon', 'knife', 'ladle']


# iterable
# use the range() function to create an iterable
numbersList = [number for number in range(5)]
print(numbersList)
# [0, 1, 2, 3, 4]

someNumbers = [x for x in range(10) if x<11]
print(someNumbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# _______Expression________

grades = ["a", "b","c", "c", "a", "a", "b"]

#Set the values in the new list to upper case
newGrades = [x.upper() for x in grades]
print(newGrades)
# ['A', 'B', 'C', 'C', 'A', 'A', 'B']

#Set all values in the new list to 'A'
newGrades = ['A' for x in grades]
print(newGrades)
# ['A', 'A', 'A', 'A', 'A', 'A', 'A']

#Return "B" instead of "C"
newGrades = [x if x!="c" else "b" for x in grades]

#return the item if it's not C, if it's C return B

print(newGrades)
#['a', 'b', 'b', 'b', 'a', 'a', 'b']




#-------------------  Sort Lists  ---------------------

#_______Sort List Alphanumerically
# sort()
comedians = ["Ji Hyo", "jae Suk", "Suk Jin", "kwang Soo", "So Min"]

comedians.sort()
print(comedians)
#['Ji Hyo', 'So Min', 'Suk Jin', 'jae Suk', 'kwang Soo']
# capital letter comes first

savings = [100,50,65,82,65]
savings.sort()
print(savings)
#[50, 65, 65, 82, 100]



#_________Sort descending
# reverse = True
comedians.sort(reverse =True)
print(comedians)
#['kwang Soo', 'jae Suk', 'Suk Jin', 'So Min', 'Ji Hyo']



#________Customize Sort Function
# key = function

def myFunc(n):
  return abs(n-60)

savings.sort(key=myFunc)
print(savings)
#[65, 65, 50, 82, 100]
# Sort the list based on how close the number is to 60



#________Case Insensitive Sort
comedians.sort(key =str.lower)
print(comedians)
#['jae Suk', 'Ji Hyo', 'kwang Soo', 'So Min', 'Suk Jin']


# reverse order
comedians.reverse()
print(comedians)
#['Suk Jin', 'So Min', 'kwang Soo', 'Ji Hyo', 'jae Suk']




#-------------------  Copy Lists  ---------------------

# copy()
actors = comedians.copy()
print(actors)
#['Suk Jin', 'So Min', 'kwang Soo', 'Ji Hyo', 'jae Suk']

# list()
teachers = ["Suzi","Buana","Lorry","Trisha"]
leaders = list(teachers)
print(leaders)
#['Suzi', 'Buana', 'Lorry', 'Trisha']


#-------------------  Join Lists  ---------------------

list1= ["a","b","c"]
list2= [1,2,3]

#1
list3= list1 + list2
print(list3)
#['a', 'b', 'c', 1, 2, 3]

#2
# for x in list2:
#   list1.append(x)
# print(list1)
#['a', 'b', 'c', 1, 2, 3]

#3
list1.extend(list2)
print(list1)
#['a', 'b', 'c', 1, 2, 3]


#-------------------  List Method  --------------------


# Python has a set of built-in methods that you can use on lists.

# Method	    Description
# append()	  Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	  Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	  Adds an element at the specified position
# pop()	      Removes the element at the specified position
# remove()	  Removes the item with the specified value
# reverse()	  Reverses the order of the list
# sort()	    Sorts the list


