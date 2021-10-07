# Strings, you know what they are
# NOT character arrays in python, oh wait python doesn't even have arrays ...
# Declaring strings of songs by my favorite artist ~KESHI~ <3
keshi1 = "beside you"
keshi2 = "like i need u"

# String methods
# split() -> separates string on specified parameter (whitespace) to list of strings
print("like i need u".split(" "))

# print("abcde".split(""))
# can not split because no separator defined "" - nothing to split on

# find index of character (or substring)
# finds index of FIRST occurence in string
print(keshi2.index("i"))
# returns index where substring begins - in this case the y in you is at index 7
print(keshi1.index("you"))

# upper() lower() changes to upper or lowercase
# returns copy of string in uppercase
print(keshi1.upper())
print(keshi1.upper().lower())
# does not change original string
print(keshi1)

# replace a word with a different one in string .replace(x, y)
# let's use proper grammer keshi
print("like i need u".replace("u", "you"))

# in keyword to find if one string is in another
print('you' in keshi2)
# still no grammar

# length of a string - len()
print(len(keshi1))


# String dissection in Python
# str[index] -> chooses one letter at index
# str[-index] -> index backwards from end
# str[start : end] -> get a range of letters from start to end
# str[start:end:step] -> range of letters taking step sized steps between
# str[:end] -> omit start index and grab letters from zerup up to end
# str[start:] -> omit end index and grab letters from start up to end of string
# str[::-1] -> reverses a string by going backwards with a step of -1 from start to end
