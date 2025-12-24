
def count_categories(s: str):
    vowels = set("aeiouAEIOU")
    counts = {"vowels": 0, "consonants": 0, "digits": 0, "special": 0}

    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                counts["vowels"] += 1
            else:
                counts["consonants"] += 1
        elif ch.isdigit():
            counts["digits"] += 1
        else:
            counts["special"] += 1
    return counts

text = "Vodafone G.E.T. 2025! #Pune"
result = count_categories(text)
print("Input:", text)
print("Counts:", result)
