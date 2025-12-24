
def remove_common_from_first(a: set, b: set):
    return a - b


A = {1, 2, 3, 4}
B = {3, 4, 5}
print(remove_common_from_first(A, B))