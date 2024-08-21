def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception("Modular inverse doesn't exist")
    return x % phi

def factor_modulus(N):
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return i, N // i
    return None, None

def calculate_private_exponent(N, e):
    p, q = factor_modulus(N)
    if p is None or q is None:
        print("Failed to factor modulus")
        return None
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return d

# Test Factoring and Private Exponent Calculation
N = 221  # Example small modulus
e = 5   # Public exponent
d = calculate_private_exponent(N, e)
if d:
    print(f"Calculated private exponent d: {d}")
