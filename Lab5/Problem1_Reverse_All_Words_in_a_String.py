text = "hello .py"

words = text.split()
result = ""

for word in words:
    result += word[::-1] + " "

print("Reversed String:", result.strip())