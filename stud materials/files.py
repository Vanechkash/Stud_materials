file = open('myfile.txt', 'w')

file.write('hello world')

file.close()

file = open('myfile.txt', 'w')
file.close()

file = open('myfile.txt')

file.read()
file.close()

with open('myfile.txt') as file:
    print(file.read())

with open('myfile.txt') as file:
    for i in file:
        print(i, end='')

s = 0
with open('test.txt') as file:
    for i in file:
        s += float(i)
print(s)