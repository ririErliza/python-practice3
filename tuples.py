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

#Remove Items
# Note: You cannot remove items in a tuple.

# Tuples are unchangeable, so you cannot remove items from it, but you can
#  use the same workaround as we used for changing and adding tuple items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
# ('banana', 'cherry')

# The del keyword can delete the tuple completely
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists


#-------------------  Unpack Tuple  -----------------------

# When we create a tuple, we normally assign values to it.
#  This is called "packing" a tuple
# But, in Python, we are also allowed to extract the values back into variables.
#  This is called "unpacking"

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# apple
# banana
# cherry

# Using Asterisk*
# If the number of variables is less than the number of values,
#  you can add an * to the variable name and the values will be
#  assigned to the variable as a list

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# apple
# banana
# ['cherry', 'strawberry', 'raspberry']



#-------------------  Loop Tuple  -------------------------

#iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# apple
# banana
# cherry

# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# apple
# banana
# cherry

# Using a While Loop
thistuple = ("ding", "dang", "deng")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# ding
# dang
# deng

#-------------------  Join Tuple  -------------------------

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#('a', 'b', 'c', 1, 2, 3)

# Multiply Tuples
fruits = ("Tip", "Tap", "Top")
mytuple = fruits * 2

print(mytuple)
# ('Tip', 'Tap', 'Top', 'Tip', 'Tap', 'Top')

#------------------  Tuple Methods  -----------------------

# count()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5) # The count() method returns the number
                       # of times a specified value appears in the tuple
print(x)
# 2

# index()
thistuple_a = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
y = thistuple_a.index(8) # Searches the tuple for a specified value and
                         # returns the position of where it was found
print(y)
# 3
