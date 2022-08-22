import time
seconds = int(time.time())

print(seconds)

if seconds % 15 == 0:
  print("FizzBuzz")
elif seconds % 3 == 0:
  print("Fizz")
elif seconds % 5 == 0:
  print("Buzz")
else:
  print("seconds")