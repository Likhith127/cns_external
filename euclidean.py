def euclidean(a, b):
    while b:
        a, b = b, a % b
    return a
def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
a = 48
b = 18
gcd_normal = euclidean(a, b)
print("GCD (Normal Euclidean) of", a, "and", b, "is:", gcd_normal)
gcd_extended, x, y = extended_euclidean(a, b)
print("GCD (Extended Euclidean) of", a, "and", b, "is:", gcd_extended)
print("Coefficients x and y are:", x, "and", y)