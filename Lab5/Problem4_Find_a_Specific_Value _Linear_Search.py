numbers = [10, 20, 30, 40, 50]
text = int(input("Enter a number to search: "))

for number in numbers:
    if number == text:
        print("Found")
        break
else:
    print("Not Found")