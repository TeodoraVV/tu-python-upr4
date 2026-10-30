n = int(input("Въведете цяло число: "))

cifri = []
for c in str(abs(n)):
    cifri.append(int(c))

prav = tuple(cifri)
obraten = tuple(cifri[::-1])

print("Прав ред:", prav)
print("Обратен ред:", obraten)
