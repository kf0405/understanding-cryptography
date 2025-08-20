def trivium_warmup(n_bits):
    A = [0]*93
    B = [0]*84
    C = [0]*111
    C[110] = 1

    warmup_bits = []
    for _ in range(n_bits):
        t1 = A[65] ^ (A[90] & A[91]) ^ A[92] ^ B[68]
        t2 = B[68] ^ (B[81] & B[82]) ^ B[83] ^ C[108]
        t3 = C[65] ^ (C[108] & C[109]) ^ C[110] ^ A[68]

        z = t1 ^ t2 ^ t3 # bit generated at each step
        warmup_bits.append(z)

        A = [t1] + A[:92] #adds value and limits registers to 92, 83, 110.
        B = [t2] + B[:83]
        C = [t3] + C[:110]

    return warmup_bits


warmup_70 = trivium_warmup(70)
print(warmup_70)
