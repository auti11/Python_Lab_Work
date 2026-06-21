number = [12,11,3,4,90,2,45,36,78,56,23,89,67]
maximum = number[0]
minimum = number[0]
for index in number:
    if index > maximum:
        maximum = index
    if index < minimum:
        minimum = index
print("Maximum number is: ", maximum)
print("Minimum number is: ", minimum)