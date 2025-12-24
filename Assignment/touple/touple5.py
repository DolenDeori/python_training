
def swap_tuples_unpack(a: tuple, b: tuple):
    a, b = b, a
    return a, b


t1 = (1, 2, 3)
t2 = ("Vodafone", "Pune")
t1, t2 = swap_tuples_unpack(t1, t2)


print(t1)
print(t2)
