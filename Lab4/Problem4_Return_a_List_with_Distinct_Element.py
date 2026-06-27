def distinct_elements(lst):
    unique = []

    for item in lst:
        if item not in unique:
            unique.append(item)

    return unique


numbers = [1, 2, 3, 3, 3, 3, 4, 5]

print("Original List:", numbers)
print("Distinct List:", distinct_elements(numbers))