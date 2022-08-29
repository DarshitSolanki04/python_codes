# Exponent function for only non-negative integers

x = 1


def exponent(base, exp):
    global x
    y = exp
    while y > 0:
        x *= base
        y -= 1
    return base, exp


baSe, eXp = exponent(5, 4)
print('\n', baSe, 'raised to the power', eXp, ':', x)
