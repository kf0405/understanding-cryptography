alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)] + [str(i) for i in range(6)] #from A to 5
val2sym = {i: alphabet[i] for i in range(len(alphabet))}  #convert from alphabet to numeric value
sym2val = {v: k for k, v in val2sym.items()} #opposite conversion

def to_bits(val):
    return [(val >> (4-i)) & 1 for i in range(5)]  # 5-bit version of the value

def from_bits(bits):
    val = sum(b << (4-i) for i,b in enumerate(bits))
    return val2sym[val]

def lfsr(iv, length):
    state = iv[:]  # list of 6 bits
    seq = []
    for _ in range(length):
        out = state[0]
        seq.append(out)
        # feedback = leftmost ^ next 
        fb = state[0] ^ state[1] #XOR
        state = state[1:] + [fb]
    return seq

cipher = "J5A0EDJ2B"

cipher_bits = []
for c in cipher:
    val = sym2val[c]
    cipher_bits.extend(to_bits(val))

ks = lfsr([1,1,1,1,1,1], len(cipher_bits))

plain_bits = [c ^ k for c,k in zip(cipher_bits, ks)]

plaintext = ""
for i in range(0, len(plain_bits), 5):
    block = plain_bits[i:i+5]
    plaintext += from_bits(block)

print(plaintext)
