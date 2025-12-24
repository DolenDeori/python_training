
def count_occurrence_no_builtin(t: tuple, target):
    count = 0
    for x in t:
        if x == target:
            count += 1
    return count

t = (1, 2, 3, 2, 2, 5)
print(count_occurrence_no_builtin(t, 2))
print(count_occurrence_no_builtin(t, 7))

