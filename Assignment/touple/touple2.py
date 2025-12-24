
def list_of_tuples_to_dict_basic(pairs: list[tuple]):
    return dict(pairs)

pairs = [("hi", 1), ("hello", 2), ("good bye", 99)]
d = list_of_tuples_to_dict_basic(pairs)
print(d)
