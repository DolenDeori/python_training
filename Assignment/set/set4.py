
def print_greater_than(s: set[int | float], threshold: int | float):
    for x in s:
        if x > threshold:
            print(x)


S = {5, 1, 9, 3, 7}
print_greater_than(S, 4)

def get_greater_than_sorted(s: set[int | float], threshold: int | float) -> list:
    return sorted([x for x in s if x > threshold])

print(get_greater_than_sorted(S, 4))  # [5, 7, 9]
