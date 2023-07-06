# List ["item", "item","item" ]
# Tuple ("item", "item","item" )
# SET {"item", "item","item" }
# Dictionary {"key":"value", "key":"value", "key":"value"}


# Duplicates Not Allowed
# Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#Length of a Set
print(len(thisset))

#Data Types
set1 = {"apple", "banana", "cherry"} #string
set2 = {1, 5, 7, 9, 3} #int
set3 = {True, False, False} #boolean
set4 = {"abc", 34, True, 40, "male"} #mix

#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
# {'cherry', 'banana', 'apple'}

#----------- Access Set Items -----------------------
#---------------- Add Set Items  --------------------
#--------------- Remove Set Items  ------------------
#------------------- Loop Sets  ---------------------
#------------------- Join Sets  ---------------------
#----------------- Set Methods  ---------------------