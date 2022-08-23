my_list = ["Cat", "Mouse", "Frog"]

# Write some code to amend the list here. Should print ['Mouse', 'Lynx', 'Cat', 'Frog']

my_list.insert(1,"Lynx")
my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)