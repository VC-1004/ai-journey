marks = [75, 85, 90, 64]
marks[1] = 88
print(marks)

marks = [75, 85, 90, 64, 77]
print(marks[1:3]) # starts at position 1 and stops before position 3
print(marks[:2]) # starts from the start and stops before position 2
print(marks[2:]) # starts at position 2 and till the end (including the last element)
print(marks[-2:]) # the last two eleemnts of the list
print(marks[::-1]) # reverses the list

marks.append(95) # adds 95 to the end of the list
marks.insert(0, 50) # adds 50 to the position 0 of the listand everything else shifts to the right
print(marks)

print(marks.count(90)) # counts the number of occurrences of 90 in the list
print(marks.index(90)) # returns the index of the first occurrence of 90 in the list

marks.remove(90) # removes the first occurrence of 90 from the list
print(marks)
element2 = marks.pop(2) # removes the element at position 2 and will store it in the variable element2 and marks.pop() will remove the last element of the list and do the same work
print(marks)
print(element2)

print(77 in marks) # checks if 77 is in the list and returns True or False

marks.sort() # sorts the list in ascending order
print(marks)
marks.sort(reverse=True) # sorts the list in descending order
print(marks)
# If I write new = sorted(marks) then it will sort the list and store it in new but the original list will remain unchanged

# Useful Built-Ins:  
print(len(marks)) # returns the length of the list
print(sum(marks)) # returns the sum of all the elements in the list
print(min(marks)) # returns the minimum value in the list
print(max(marks)) # returns the maximum value in the list

point = (3, 7) # tuple
rgb = (255, 128, 0) 

print(point[0])       
print(rgb[1:])        
print(len(rgb))       
print(255 in rgb)     
for value in rgb:
    print(value)

x, y = point # unpacking the tuple
print(x, y)

a = (5) # This is not a tuple, it's an integer
b = (5,) # This is a tuple with one element

s = {4, 2, 4, 9, 2} # set
print(s) # prints the set without duplicates and without any specific order
print(len(s)) 

s.add(5) # adds 5 to the set
s.add(4) # does nothing because 4 is already in the set
s.remove(2) # removes 2 from the set and prints error if 2 is not in the set
s.discard(2) # removes 2 from the set and doesn't print error if 2 is not in the set
print(s)

# print(s[0]) This will give an error because sets are unordered and don't support indexing

# Finding a time complexity in finding an element in a list and a tuple is O(n) because it has to check each element one by one, while in a set it is O(1) because it finds the element directly.

nums = [3, 1, 3, 2, 1]
unique_nums = set(nums) # converts the list to a set and removes duplicates
print(unique_nums)
print(len(unique_nums))

coding = {"Asha", "Ravi", "Meera"}
music = {"Ravi", "Meera", "Kabir"}
print(coding & music) # intersection of two sets
print(coding | music) # union of two sets
print(coding - music) # difference of two sets

marks = { "Asha": 85, "Ravi": 72, "Meera": 90 } # dictionary

print(marks["Asha"]) # prints the value of the key "Asha"
# print(marks["Kabir"]) # This will give an error because "Kabir" is not a key in the dictionary
# To avoid this error: 
print(marks.get("Kabir")) # prints None because "Kabir" is not a key in the dictionary
print(marks.get("Kabir", 0)) # prints 0 because "Kabir" is not a key in the dictionary and 0 is the default value but .get only reads the value and do not saves it to the dictionary

marks["Kabir"] = 78 # adds a new key-value pair to the dictionary
marks["Asha"] = 90 # updates the value of the key "Asha"

del marks["Ravi"] # deletes the key-value pair with the key "Ravi"
print(marks)

print("Asha" in marks) # checks if "Asha" is a key in the dictionary and returns True or False
print("Ravi" not in marks) # checks if "Ravi" is not a key in the dictionary and returns True or False
print(75 in marks.values()) # checks if 75 is a value in the dictionary and returns True or False
print(75 in marks) # checks if 75 is a key (not value) in the dictionary and returns True or False

for name in marks: # iterates over the keys of the dictionary
    print(name) 

for name, mark in marks.items(): # iterates over the key-value pairs of the dictionary, and .items() returns a list of tuples where each tuple is a key-value pair
    print(name, mark)

# We can also use .keys() and .values() to iterate over the keys and values of the dictionary respectively
# len(marks) returns the number of key-value pairs in the dictionary

# To count the number of occurrences of each element in a list, we can use a dictionary. 
fruits = ["apple", "banana", "apple", "mango", "apple"]
count = {}
for f in fruits:
    if f in count:
        count[f] = count[f] + 1
    else:
        count[f] = 1
print(count)