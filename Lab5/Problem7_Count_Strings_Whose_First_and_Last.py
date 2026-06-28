words = ['aca', 'xyz', 'aba', '1221']
print("Original List:", words)
count = 0

for word in words:
    if len(word) >= 2:
        if word[0] == word[-1]:
            count = count + 1

print("Count =", count)