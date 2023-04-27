def isPalindrome(string: str):
    return string == ''.join(reversed(string))


assert isPalindrome("hello") == False
assert isPalindrome("kajak") == True
assert isPalindrome("abccba") == True
