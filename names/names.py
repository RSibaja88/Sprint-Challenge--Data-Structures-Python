import time
from binarySearchTree import BSTNode

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

binarySearchTree = BSTNode("None") #return first names

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
nodes = BSTNode('names')
duplicates = set.intersection(set(names_1),set(names_2))
'''for names in names_1:
    nodes.insert(names)

for name in names_2:
    if nodes.contains(name):
        duplicates.append(name)'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
