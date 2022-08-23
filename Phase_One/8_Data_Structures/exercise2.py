my_list = ["Cat", "cat", "frog", "cat", "dog", "Dog"]
counters = {}

# Write some code to count the items in the list here. Should print (in any order)
# { 'cat': 3, 'dog': 2, 'frog': 1 }

for animal in my_list:
  if animal.lower() in counters:
    counters[animal.lower()] += 1
  else:
    counters[animal.lower()] = 1

print(counters)