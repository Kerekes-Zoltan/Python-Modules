import decimal

val_pi = decimal.Decimal(3.1415)

print("Create a Decimal from a float: ", val_pi, "\n", val_pi.as_tuple())

string_n = decimal.Decimal(123.123)
print("\nCreate a Decimal from a String: ", string_n, "\n", string_n.as_tuple())