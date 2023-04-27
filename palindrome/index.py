def isPalindrome(string: str):
    return string == string[::-1]


assert isPalindrome("hello") == False
assert isPalindrome("kajak") == True
assert isPalindrome("abccba") == True
