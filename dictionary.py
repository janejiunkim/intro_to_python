# DICTIONARIES - key-calue pairs like a js object
# Keys must be hashable, must be immutable (String or number)

# Create an empty dictionary
Dict = {}
print(Dict)
# => {}

# Adding elements one at a time
Dict[0] = 'first'
Dict[2] = 'second'
Dict[4] = 3

print(Dict)

# Adding set of values to a single key
Dict['value_set'] = 2, 3, 4
print(Dict)

# Reassigning values 
# updating an existing key's value
Dict[2] = 'third'
print(Dict)

# Can put dictionaries inside dictionaries (Nested Dictionaries!)
# store 5 in variable five
five = 5
# 5 is now a key of Dict with the value of {'Nested': {...}}
Dict[five] = {'Nested': {'1' : 'Goodbye', '2' : 'Friends'}}
print(Dict)

# NOTE: can have two keys that are same, but last value will be kept

# Looping through dictionary
# similar to for or foreach loop
for key in Dict:
    print(Dict[key])