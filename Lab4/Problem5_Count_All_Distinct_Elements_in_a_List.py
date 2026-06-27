def count_distinct(lst):
    counted = []

    for item in lst:
        if item not in counted:
            print(item, "=>", lst.count(item))
            counted.append(item)


numbers = [10, 20, 30, 30, 30, 30, 20, 40]

count_distinct(numbers)