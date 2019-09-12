from doctest import testmod
testmod()

def fact(x):
    '''
    >>> fact(5)
    120
    >>> fact("stroka")
    Traceback (most recent call last):
        ...
    ValueError: value must be integer!
    '''
    if type(x) != int:
        raise ValueError('value must be integer!')
    return x * fact(x - 1) if x else 1



print(fact.__doc__)