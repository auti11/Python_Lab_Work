def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1
my_list = [10, 20, 30, 40, 50]

value_for_search = int(input("Enter a value to search for: "))

result = linearSearch(my_list, value_for_search)
if result != -1:
    print(value_for_search, "is found in the list at index", result)
else:
    print(value_for_search, "is not found in the list.")
