sample_string = input("Enter a string: ")
words = sample_string.split()
reversed_words = words[::-1]
reversed_string = " ".join(reversed_words)
print(reversed_string)