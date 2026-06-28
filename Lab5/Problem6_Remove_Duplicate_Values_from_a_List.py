numbers = [10, 20, 30, 20, 50]
print("Original List:", numbers)
new_list = []

for num in numbers:
    if num not in new_list:
        new_list.append(num)

print( "New List:",new_list)