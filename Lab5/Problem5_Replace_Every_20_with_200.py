List = [10, 20, 30, 20, 50]
print("Original List:", List)
value = 20

for i in range(len(List)):
    if List[i] == value:
        List[i] = 200

print("Updated List:", List)