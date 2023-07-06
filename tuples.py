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

#Nothing found





#-------------------  Update Tuple  -----------------------

#Change Tuple Values
#Once a tuple is created, you cannot change its values.
#  Tuples are unchangeable, or immutable as it also is called.

#But there is a workaround. You can convert the tuple into a list,
#  change the list, and convert the list back into a tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1]="kiwi"
x=tuple(y)

print(x)
# ('apple', 'kiwi', 'cherry')


# Add Items
# Since tuples are immutable, they do not have a built-in append() method,
#  but there are other ways to add items to a tuple.

# 1. Convert into a list: Just like the workaround for changing a tuple,
#  you can convert it into a list, add your item(s), and convert it back
#  into a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)
# ('apple', 'banana', 'cherry', 'orange')


# 2. 2. Add tuple to a tuple. You are allowed to add tuples to tuples,
#  so if you want to add one item, (or many), create a new tuple with
#  the item(s), and add it to the existing tuple

fruitsTup = ("apple", "banana", "cherry")
y=("orange", )
fruitsTup += y

print(fruitsTup)
# ('apple', 'banana', 'cherry', 'orange')

#-------------------  Unpack Tuple  -----------------------

#-------------------  Loop Tuple  -------------------------

#-------------------  Join Tuple  -------------------------

#------------------  Tuple Methods  -----------------------
