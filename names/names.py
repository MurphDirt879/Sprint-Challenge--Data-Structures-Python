import time

start_time = time.time()

from BinarySearchTree import BinarySearchTree

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

searchTree = BinarySearchTree("") 

for name in names_1:
    searchTree.insert(name)
for name in names_2: 
    if searchTree.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

stretchstart_time = time.time()

nameList = []
stretchDuplicates = []

for name in names_1:
        nameList.append(nameList)
for name in names_2:
    if name in nameList:
        stretchDuplicates.append(name)

stretchend_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {stretchend_time - stretchstart_time} seconds")

# Of course is is going to be slower .... difference for my computer is 0.145 (BST) vs 1.90 (Array).