number = [10, 20, 30, 20, 50]
print("Original list:", number)
for i in range(len(number)):
    if number[i] == 20:
        number[i] = 200
print("List after replacing 20 with 200:", number)