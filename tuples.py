# TUPLE ("item", "item","item" )
# List ["item", "item","item" ]
# Set {"item", "item","item" }
# Dictionary {"key":"value", "key":"value", "key":"value"}


# Tuple Items
# Tuple items are ordered, UNchangeable, and allow duplicate values.
# Tuple items are indexed

thistuple = ("a", "b", "c")
print(thistuple)
#('a', 'b', 'c')

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove
#  items after the tuple has been created



# Tuple Length
print(len(thistuple))
# 3


# One item tuple, remember the comma
fruits = ("apple",)
print(type(fruits)) #<class 'tuple'>

#NOT a tuple
fruits = ("apple")
print(type(fruits)) #<class 'str'>


#Data types
tuple1 = ("apple", "banana", "cherry") #string
tuple2 = (1, 5, 7, 9, 3) #number
tuple3 = (True, False, False) #boolean
tuple4 = ("abc", 34, True, 40, "male") #mix


# tuple() Constructor
# Using the tuple() method to make a tuple

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
# ('apple', 'banana', 'cherry')


#-------------------  Access Tuple  -----------------------
# access tuple items by referring to the index number,
#  inside square brackets

print(thistuple[1])
#banana

print(thistuple[-1])
#cherry

print(thistuple[1:3])
#('banana', 'cherry')

print(thistuple[:2])
#('apple', 'banana')

print(thistuple[1:])
#('banana', 'cherry')

print(thistuple[-3:-1])
#('apple', 'banana')

# Check if Item Exists
# use the in keyword

if "mango" in thistuple:
  print("Yes, found in tuple")
else:
  print("Nothing found")





#-------------------  Update Tuple  -----------------------

#-------------------  Unpack Tuple  -----------------------

#-------------------  Loop Tuple  -------------------------

#-------------------  Join Tuple  -------------------------

#------------------  Tuple Methods  -----------------------
