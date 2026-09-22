def is_palindrome(text):
    text=text.lower()
    return text==text[::-1]

word=input()
print(is_palindrome(word))