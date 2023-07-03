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


# Access Items
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

#  Check if item exists
if "coconut" in thislist3:
  print("Yes, 'apple' is in the fruits list")
else:
  print("This fruit is not in the list")

# This fruit is not in the list



