text = input("Въведете текст: ")

d = {}
for ch in text:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print("Речникът има", len(d), "елемента:")
for key in sorted(d):
    print(key + ":" + str(d[key]), end=" ")
print()
