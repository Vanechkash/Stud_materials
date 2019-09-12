from time import time
start = time()


##### do


print(time() - start)

% % time
limit = 10 ** 5
maxsteps = 0
bestdigit = 0

for digit in range(2, limit):  # 13.2|10.4|9.7|7.21
    cur = digit
    steps = 0
    while cur != 1:
        if not cur % 2:
            cur //= 2
            steps += 1
        else:
            cur = (cur * 3 + 1) // 2
            steps += 2

    if steps > maxsteps:
        maxsteps = steps
        bestdigit = digit

print("bestdigit is {:}, maxsteps is {:}".format(bestdigit, maxsteps))




%%time
limit = 10 ** 6


def colatz(l):
    r = {}
    for digit in range(2, l):#13.2|10.4|9.7|7.21|0.68|0.494
        cur = digit
        steps = 0
        while cur != 1:
            if not cur % 2:
                cur //= 2
                steps += 1
            else:
                cur = (cur * 3 + 1) // 2
                steps += 2
            if cur in r:
                steps += r[cur]
                break
        r[digit] = steps
    return r

response = colatz(limit)



