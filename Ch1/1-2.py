from collections import Counter

def frequency_ciphertext(cipher):
    clean_text = cipher.replace("\n", "").replace(" ", "")
    freq = Counter(clean_text)
    return [i[0] for i in freq.most_common()]

def decrypt(cipher):
    freq = frequency_ciphertext(cipher)
    english_frequency = ["E","T","A","O","I","N","S","R","H","D","L",
        "U","C","M","F","Y","W","G","P","B","V","K","X","Q","J","Z"]
    keymap = zip(freq, english_frequency )
    for x, y in keymap:
        cipher = cipher.replace(x, y)
    return cipher

def manual_decrypt(cipher, keymap):
    for x, y in keymap:
            cipher = cipher.replace(x, y)
    return cipher

with open("cipher1-2.txt", "r") as f:
    cipher = f.read()

plaintext = decrypt(cipher)
print(plaintext)

'''
ACOEINNLUATEOEOANNMILRETHESAFESRTDRTIAUTHEYSEITOITESROATHTHEASWNDDGP
Statistical approach doesnt work, so we should brute force possible shifts
'''

def shift_cipher_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)

def shift_cipher_decrypt(text, shift):
    return shift_cipher_encrypt(text, -shift)

for num in range(0,27):
    decrypted = shift_cipher_decrypt(cipher, num)
    print(decrypted)

'''
ifweallunitewewillcausetheriverstostainthegreatwaterswiththeirblood.
letters were shifted by 15
'''
