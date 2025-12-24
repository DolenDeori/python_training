
t = ([10, 20, 30], {"city": "Pune", "role": "GET"})
print("Original:", t)


t[0].append(40)
t[0][1] = 25

t[1]["role"] = "Engineer Trainee"
t[1]["company"] = "Vodafone"

print("Modified:", t)
