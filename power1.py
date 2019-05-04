def puissance(a, n):
    nb = a
    while n != 1:
        a *= nb
        n -= 1
    return a

numb = puissance(4, 3)
print(numb)