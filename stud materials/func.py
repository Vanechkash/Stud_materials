def mysum(x, y):
    return x + y


res = mysum(3, 5)
print(res)

%%time
def f():
    limit = 10 ** 4 # 2.75 | 2.56 | 2.42 | 1.2 | 0.6
    y = [2]

    for digit in range(3, limit, 2):
        for i in range(3, digit // 2 + 1, 2):
            if not digit % i:
                break
        else:
            y.append(digit)
f()

def myfun(justfun):
    res = justfun(3, 4)
    return res

def f1(x,y):
    return x + y

myfun(f1)

def hello():
    print('hello')

def myfun(fun): # decor
    def justfun():
        print('before')
        fun()
        print('aft')
    return justfun

hello()

hello = myfun(hello)# use decor
hello()


@myfun
@myfun
@myfun
@myfun
@myfun
@myfun
@myfun
@myfun
def hell():
    print('hello')


hell()


def decor1(fun):
    def newfun(x):
        return "хлеб\n" + fun(x) + "\nхлеб"

    return newfun


def decor2(fun):
    def newfun(x):
        return 'помидор\n' + fun(x) + '\nпомидор'

    return newfun


def decor3(fun):
    def newfun(x):
        return 'сыр\n' + fun(x) + '\nсыр'

    return newfun


@decor1
@decor2
@decor3
def hell(x):
    return x


print(hell('мясощщщщщ'))

def decor_for_decor(word):
    def decor3(fun):
        def newfun(x):
            return word + '\n' + fun(x) + '\n' + word
        return newfun
    return decor3


@decor_for_decor('хлеб')
@decor_for_decor('помидор')
@decor_for_decor('сыр')
def hell(x):
    return x

print(hell('мясо'))



def avr():#замыкание
    x = []
    def avr(y):
        nonlocal x
        x.append(y)
        return sum(x) / len(x)
    return avr

avr = avr()
avr(5)
avr(7)


def fact(x):
    return x * fact(x - 1) if x else 1
fact(5)


n = 5
[[0 if i != j else 1 for i in range(n)] for j in range(n)]