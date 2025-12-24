
def set_operations(a: set, b: set):
    return {
        "union": a | b,
        "intersection": a & b,
        "difference_a_minus_b": a - b,
        "difference_b_minus_a": b - a,
        "symmetric_difference": a ^ b,
    }

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
ops = set_operations(A, B)
print("A:", A)
print("B:", B)
for k, v in ops.items():
    print(f"{k}: {v}")
