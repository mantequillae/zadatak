z = "Na vrh brda vrba..."
print(z)
y = "mrda"

for f in range(0,11):
    x = input('> ')
    if x == y:
        print("Well done!", z + y)
        exit(0)

print("And then something else.")