from re import compile as regex, sub


def isPalindrome(string: str):
    string = sub(regex('\s'), '', string)
    return string == string[::-1]


assert isPalindrome("hello") == False
assert isPalindrome("kajak") == True
assert isPalindrome("abccba") == True
assert isPalindrome("ni talar bra latin") == True
