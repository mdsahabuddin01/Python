#Python: Palindrome Checker (Ignoring Case, Spaces & Punctuation)
def IsPalindrome(text: str) -> bool:

  CleanTxt = ''.join(char.lower() for char in text if char != " ")
  return CleanTxt == CleanTxt[::-1]

examples = [
    "level",
    "python",
    "Race car",
    "Never odd or even",
    "Hello",
    "123321",
]

for word in examples:
    if IsPalindrome(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
