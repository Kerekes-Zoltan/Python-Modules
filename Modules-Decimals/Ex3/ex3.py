from decimal import Decimal

def round_decimal(x):
    remainder = x.remainder_near(Decimal('0.10'))
    if abs(remainder) == Decimal('0.05'):
        return x
    else:
        return x - remainder

# Test code.
for x in range(80, 90):
    y = Decimal(x) / Decimal('1E2')
    print("{0} rounds to {1}".format(y, round_decimal(y)))