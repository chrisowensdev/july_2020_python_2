replace = (("A", "4"), ("E", "3"), ("G", "6"),
           ("I", "1"), ("O", "0"), ("S", "5"), ("T", "7"))

string = "I am a leet programmer"

upperstring = string.upper()

for old, new in replace:
    upperstring = upperstring.replace(old, new)


lowerstring = upperstring.lower()
print(lowerstring[0].upper() + lowerstring[1:])
