# Exponent function for only non-negative integers.


x = 1


def exponent(base, exp):
    '''
    This function calculates the exponent of a number.
    '''
    global x  # Will add the comment later.
    y = exp
    while y > 0:
        x *= base  # Equivalent to x = x * base.
        y -= 1  # Similarly, y = y - 1.
    return base, exp


baSe, eXp = exponent(5, 4)  # LOOK HERE FIRST. When looking at code that is not your own, looking at functions first can make you confused.
# In the line above we are passing 2 values to the exponent function, 5 as base and 4 as exp, we are recieving the values of base and exp (that are returned by the function) in baSe and eXp.
print('\n', baSe, 'raised to the power', eXp, ':', x)
