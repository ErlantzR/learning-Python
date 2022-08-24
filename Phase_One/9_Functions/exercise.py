# Your code goes here.

def add_five(number):
  return number + 5

print(add_five(4))
# Should print: "9"

print(add_five(2132))
# Should print: "2137"

# Your code goes here.

def subtract_low_from_high(a, b):
  return abs(a - b)

print(subtract_low_from_high(2, 3))
# Should print "1"

print(subtract_low_from_high(3, 2))
# Should print "1"

print(add_five(subtract_low_from_high(1463, 16475)))
# Should print "15017"