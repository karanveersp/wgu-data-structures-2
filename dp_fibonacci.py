def rec_fibo(n):
    """some terms computed more than once"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return rec_fibo(n - 1) + rec_fibo(n - 2)

def iter_fibo(n):
    """no term computed more than once"""
    if n == 0:
        return 0
    previous = 0
    current = 1
    i = 1
    while i < n:
        nxt = previous + current
        previous = current
        current = nxt
        i += 1
    return current

