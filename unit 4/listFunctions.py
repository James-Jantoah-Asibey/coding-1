# List- a data type for collecting and organizing data.
# - Lists can contain all data types, including other lists.
# - Lists are changabke, we can update thr lists
# - Lists can contain duplicate  data.
# - we can get specific list items based on its index position.

# input is a function that allows us ti eneter data directly into
# our program from the terminal.
# data that is passed in from an input function automatically becomes
# a string.
name= input('what is your name?')
print(name)

skiiTripItems_ShoppingCart = ['gloves']
# insert() - Allows us ti enter a new list item.
# based on an index position.
# insert requires 2 arguments to work.

skiiTripItems_ShoppingCart.insert(1, 'snow boots')
skiiTripItems_ShoppingCart.insert(2, 'goggles')
print(skii_TripItems)

# append - allow us to enter a new item into a list
# without having to provide an index location. append() will
# automatically put the new item at the end of the list

skii_TripItems_ShoppingCart.append('scarf')
print(skii_TripItems)

# remove()- allow us to remove an item from a list.
# it works by specifiying what time you want to take out 

skiiTripItems_ShoppingCart.remove('scarf')
print(skii_TripItems)

# pop() - Allow us to remove the last item in a list
skii_TripItems.pop()
print(skii_TripItems)

# clear()/ del() - Allow us to delete/ remove all the 
# items in a list

del skill_tripItems

skii_TripItems