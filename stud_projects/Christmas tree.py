def elka(stroka):
    print(stroka)
    if stroka:
        elka(stroka[:-1])
    print(stroka)


elka('hello world')



def elka(stroka):
    return stroka + '\n' + elka(stroka[:-1]) if len(stroka) > 0 else ''

print(elka('hello world'))


