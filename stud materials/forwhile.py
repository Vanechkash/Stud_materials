a = [1, 2, 3, 4, 5, 6]
b = [34, 45, 56, 67, 78, 898]

c = []

for i in zip(a, b):
    c.append(i[0] + i[1])



for i in range(1, 150):
    if i % 2 == 0:
        print(i)


while True:
    x = float(input('enter the x'))
    print(100 - x)



dic = {'mama':35345, 'papa':675675676, 'brat':5675675}
for i in dic.keys():
    print(i)

for i in dic.values():
    print(i)

for i,j in dic.items():
    print(i,j)