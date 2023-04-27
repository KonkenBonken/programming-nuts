from re import compile as regex, sub


def isPalindrome(string: str):
    string = sub(regex('\s'), '', string).lower()
    return string == string[::-1]


assert isPalindrome("hello") == False
assert isPalindrome("kajak") == True
assert isPalindrome("abccba") == True
assert isPalindrome("Ni talar bra latin") == True
