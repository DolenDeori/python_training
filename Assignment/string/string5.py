s = "Vodafone"
print("Original:", s)

try:
    s[0] = "X"
except TypeError as e:
    print("Caught error (expected):", e)

s_modified = "X" + s[1:]
print("Modified via slicing+concat:", s_modified)

chars = list(s)
chars[0] = "Y"
s_modified_list = "".join(chars)
print("Modified via list conversion:", s_modified_list)

