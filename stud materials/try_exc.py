try:
    x = int(input('enter the digit  '))
except ValueError:
    print('ты ввел не то')

try:
    print(5 / x)
except ZeroDivisionError:
    print('не дели на ноль')
except TypeError:
    print('ошибка типов')
except:
    print('не известная ошибка')
else:
    print('sfsdfsd')

print('очень важный код')
print('еще более важный код')

while True:
    try:
        digit = int(input("enter the digit  "))
    except ValueError:
        print('самсинг рон')
    else:
        if 8 > digit > 3:
            break
        else:
            print('ты не прав')

print(digit)





def hello(digit):
    '''нельзя юзать 5'''
    if digit == 5:
        raise Exception('нельзя юзать 5', digit, 'are you dumb?')
    else:
        return digit