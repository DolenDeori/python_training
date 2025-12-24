
from collections import Counter

def char_frequency(s: str):
    return dict(Counter(s))

text = "Hello I am Dolen"
freq = char_frequency(text)
print("Input:", text)
print("Frequency:", freq)
