def encrypt_vigenere(plaintext, keyword):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_big = alpha.upper()
    if len(keyword) < len(plaintext):
        for i in range(len(plaintext) - len(keyword)):
            keyword += keyword[i % len(keyword)]
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i] in alpha:
            ciphertext += alpha[(alpha.index(plaintext[i]) + alpha.index(keyword[i])) % len(alpha)]
        elif plaintext[i] in alpha_big:
            ciphertext += alpha_big[(alpha_big.index(plaintext[i]) + alpha_big.index(keyword[i])) % len(alpha_big)]
        else:
            ciphertext += i
    return ciphertext

def decrypt_vigenere(ciphertext, keyword):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_big = alpha.upper()
    if len(keyword) < len(ciphertext):
        for i in range(len(ciphertext) - len(keyword)):
            keyword += keyword[i % len(keyword)]
    plaintext = ''
    for i in range(len(ciphertext)):
        if ciphertext[i] in alpha:
            plaintext += alpha[(alpha.index(ciphertext[i]) + len(alpha) - alpha.index(keyword[i])) % len(alpha)]
        elif ciphertext[i] in alpha_big:
            plaintext += alpha_big[(alpha_big.index(ciphertext[i]) + len(alpha_big) - alpha_big.index(keyword[i])) % len(alpha_big)]
        else:
            plaintext += i
    return plaintext

print(encrypt_vigenere('ATTACKATDAWN', 'LEMON'))
print(encrypt_vigenere("PYTHON", "A"))
print(encrypt_vigenere("python", "b"))
print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))
print(decrypt_vigenere("PYTHON", "A"))
print(decrypt_vigenere("qzuipo", "b"))