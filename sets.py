# Set -> Like List but ALL elements must be unique - NO duplicates
# UNORDERED collection data type -> iterable, mutable

# Making a set -> Curly Brackets! {}
id_set = {"jk", "ka", "si", "cc"}

# Making a set with pre-existing list - set()
id_list = ["jk","ka", "ka", "si", "cc"]
unique_ids = set(id_list)
# Python automatically removes duplicates from list 

# practice exercise
clothing_list = ['white', 'mint', 'kasai']
clothing_set = set(clothing_list)

# for loop to print the list and set out
for clothes in clothing_list:
    print(clothes)

# can not get index of a set
for clothes in clothing_set:
    print(clothes)

# Add to a set / not append because order is not guaranteed
clothing_set.add('black')
print(clothing_set)

# To remove element from set -> remove()
# Call element directly - NO INDICES, there is no real end or last element in a set
clothing_set.remove('kasai') 
print(clothing_set)