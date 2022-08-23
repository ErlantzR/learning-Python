my_cohort = [ "Luiza", "Laura", "Sam", "Anish", "Erlantz", "Simon", "Gawain", "Slava", 
            "Stevie", "Alex", "Luke", "Tom", "Tim", "Archie", "Russell", "Kyeran", 
            "Jimmy", "George", "Farzan" ]

# Program should print a dictionary with each of the letters of the alphabet
# and the number of people whose first name begins with that letter

counters = {}

for index in range(ord("a"), ord("z") + 1):
  counters[chr(index)] = 0

for name in my_cohort:
  counters[name[0].lower()] += 1

print(counters)