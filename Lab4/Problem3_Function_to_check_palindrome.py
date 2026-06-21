def palindrome_check(string):
  return string == string[::-1]
word = input("Enter a word to check if it's a palindrome: ")
if palindrome_check(word):
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")