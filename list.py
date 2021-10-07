# Create List
fps_games = ["Valorant", "Apex Legends", "Warzone"]
print(fps_games)

# Length of list
print(len(fps_games))

# Add/Append to List
fps_games.append("Rainbow Six Seige")
print(fps_games)

# Add element in list to a specific index - takes in index and element
fps_games.insert(1, "Overwatch")
print(fps_games)

# Pop -> No parameters removes last index // With parameters -> remove the items at specific index
# no parameters 
last_game = fps_games.pop()
print(last_game) 

# get rid of element at index 0 -> valorant T.T
valorant = fps_games.pop(0)
print(valorant)

print(fps_games)

# Numerical List Operations
# find sum of all numbers in list
headshots = [4, 16, 3, 1, 0, 7]
total_headshots = sum(headshots)
print("Total sum of all headshots of team:", total_headshots)

# Find smallest and largest number in list
print("Number of headshots of worst player: ", min(headshots))
print("Number of headshots of best player: ", max(headshots))

# Largest difference between numbers (max - min)
nums = [1, 10, 2, 50, 4]
big_diff = max(nums) - min(nums)
print(big_diff)
avg = (sum(nums))/len(nums)
print(avg)
