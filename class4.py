# List
# dynamic length
# mutable -> editable
# hetrogenous data types (Multiple type)
# index
# postive 0 to n-1
# negative -1 to length
# slicing
# variable names[start:end:step]
# start : int = include
# end : int = n-1
# step : int = sequance
# old way
# ->        0          1       2
names = ["Qasim","Sir Zia","Sir Inam"] # length-1 
# <-        -3       -2        -1

print(names[0]) # Qasim
print(names[-3]) # Qasim
print(names[-2]) # Sir Zia

# New method
from typing import Any
names1: list[Any] = ["Mustafa", "Zubair", "Inam", 100, True]
print(names1[-2]) #100

characters: list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(characters)

characters1: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Default slicing from left to right
# print(characters1[0:2]) 
# print(characters1[:2])
# print(characters1[0:2:1])
# print(characters1[-26:-24]) # -26:A to -24-1=-25:B
# print(characters1[::])
# print(characters1[::2])
# print(characters1[1:-3])
# print(characters1[::-1]) # Reverse the complete list

names2 : list[Any] = ["Jabbar", "Ayub", "Dakkan", True, 33]
# print(names2)
# del names2[2]
# print(names2)

# q : str = print("ABCD")  # non-return function
# print(q)

# w : str = id("ABCD")  # return function
# print(w)

# List methods
[i for i in dir(list) if "__" not in i]
['append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']

# Help method
# help(object)
# object?
# object??
# ?object
# ??object

# help(print)

# POP Method (Return function)
names3 : list[Any] = ["Jabbar", "Ayub", "Dakkan", True, 33]
# return_value : str = names3.pop() # removes last elem
return_value : str = names3.pop(1) 
print(return_value)

# Append Method(Add element in list)
# Add element in last
newList : list[str] = []
newList.append("ABBAS") 
newList.append("PIAIC")
newList.append("SMIU")
print(newList)

# Insert Method(Add element at particular index)
newList.insert(1, "Developer")
print(newList)

# Clear(Removes object only)
# newList.clear() # clears the entire list but object is remain
# print(newList)

# Copy(Returns the deep copy)
# Does changes only in the copied list 
newList2 = newList.copy()
newList2[-1] = "WEB3"
print(newList2)

# count
alpha : list[str] = ['a','a','a','b','c','c']
print(alpha.count("c"))
print(alpha.count("a"))

# Extend Method(Adds list elements into another list)
# members : list[str] = ["Sir Zia","Muhammad Qasim"] # GenAI founder members
# new_faculty_members : list[str] = ['Sir Inam',"Dr Noman"]
# members.append(new_faculty_members) # Appends the list into previous list
# print(members)

members : list[str] = ["Sir Zia","Muhammad Qasim"] # GenAI founder members
new_faculty_members : list[str] = ['Sir Inam',"Dr Noman"]
members.extend(new_faculty_members) # Adds the element one by one
print(members)

# Remove Method(remove with text value)
new_faculty_members.remove("Dr Noman")
print(new_faculty_members)

# Index Method(Returns the index)
print(members.index("Sir Inam"))

# Reverse Method(reverse the entire list)
members.reverse() # in-memory = change real data
print(members)

# Sort Method(sort in ascending order)
newlist3: list[int] = [4,2,5,3,6,1,0,8]
newlist3.sort() # in-memory = change real data sort
newlist3.sort(reverse=True) # sort in descending order
print(newlist3)