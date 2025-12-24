
def is_palindrome_slicing(s: str):
    return s == s[::-1]

def is_palindrome_indexing(s: str):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


str_1 = "madam"
str_2 = "dolen deori"
print(str_1, is_palindrome_slicing(str_1), is_palindrome_indexing(str_1))
print(str_2, is_palindrome_slicing(str_2), is_palindrome_indexing(str_2))
