import random

def is_prime(n):
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div += [n // i]
    if div == [n, 1]:
        return True
    else:
        return False


def multiplicative_inverse(e, phi):
    if e >= phi:
        u = [e, 1, 0]
        v = [phi, 0, 1]
    else:
        u = [phi, 1, 0]
        v = [e, 0, 1]
    while v[0] != 0:
        q = u[0] // v[0]
        t = [u[0] % v[0], u[1] - q * v[1], u[2] - q * v[2]]
        u = v
        v = t
    if e >= phi:
        d = u[2] % e
    else:
        d = u[2] % phi
    return d


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a + b)


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    # n = pq
    n = p * q

    # phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


print(generate_keypair(23, 43))