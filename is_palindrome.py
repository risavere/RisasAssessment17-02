def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word: ")
if is_palindrome(word):
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")