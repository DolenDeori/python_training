def is_subset(a: set, b: set):
    return a <= b

def is_proper_subset(a: set, b: set):
    return a < b


A = {1, 2}
B = {1, 2, 3, 4}
print(is_subset(A, B))
print(is_proper_subset(A, B))
print(is_subset(B, A))
