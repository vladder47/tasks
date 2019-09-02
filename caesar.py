def encrypt_caesar(plaintext, shift):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_big = alpha.upper()
    ciphertext = ''
    for i in plaintext:
        if i in alpha:
            ciphertext += alpha[(alpha.index(i) + shift) % len(alpha)]
        elif i in alpha_big:
            ciphertext += alpha_big[(alpha_big.index(i) + shift) % len(alpha_big)]
        else:
            ciphertext += i
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_big = alpha.upper()
    plaintext = ''
    for i in ciphertext:
        if i in alpha:
            plaintext += alpha[(alpha.index(i) - shift) % len(alpha)]
        elif i in alpha_big:
            plaintext += alpha_big[(alpha_big.index(i) - shift) % len(alpha_big)]
        else:
            plaintext += i
    return plaintext

print(encrypt_caesar('Python3.6', 3))
print(decrypt_caesar('Sbwkrq3.6', 3))