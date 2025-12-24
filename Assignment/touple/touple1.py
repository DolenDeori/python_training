
def tuple_min_max_builtin(t: tuple):
    if not t:
        raise ValueError("Empty tuple has no min/max")
    return min(t), max(t)

t = (7, 3, 11, -2, 8)
mn, mx = tuple_min_max_builtin(t)
print("Tuple:", t)
print("Min:", mn, "Max:", mx)
