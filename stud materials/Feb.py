a = 0
b = 1
print(a, b, sep='\n')
for i in range(98):
    print(a + b)
    c = b
    b = a + b
    a = c



%%time

feb = [0, 1]
while feb[-1] + feb[-2] < 100:
    feb.append(feb[-1] + feb[-2])

print(feb)

