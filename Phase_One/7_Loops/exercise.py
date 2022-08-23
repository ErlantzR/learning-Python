# print all numbers from 2321 to 34325 inclusive and sum all even numbers on that range
total = 0
for num in range(2321, 34326):
  print(num)
  if num % 2 == 0:
    total = total + num
print(total)