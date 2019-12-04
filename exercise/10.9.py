# Design and implement a recursive function for determining whether a string
# is a palindrome. A palindrome is a string of characters that is the same as
# the string of characters in reverse.

# string's first character equals to end character and next first character
# equals to next end character, so on. then the string is palindrome.

def palindromeString(str, first = 0, end = -1):
    """whether a string is a palindrome."""
    assert len(str) > 0, "String Must be hava one character at least."

    # first bigger or equal then length's of string then yes
    if first >= len(str):
        return True
    # Compare first with end character recursively.
    if str[first] == str[end]:
        return palindromeString(str, first + 1, end - 1)
    else :
        return False

print("asdfasdf", " is ", palindromeString("asdfasdf"))
print("asdffdsa", " is ", palindromeString("asdffdsa"))



