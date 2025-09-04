# Problems

1.   
    1. $S_1(x_1) = 14$ $S_1(x_2)= 0$, so $S_1(x_1) \oplus S_1(x_2) = 14 \neq S_1(x_1 \oplus x_2) = 0$  
    2. $S_1(x_1) = 13$ $S_1(x_2)= 4$, so $S_1(x_1) \oplus S_1(x_2) = 9 \neq S_1(x_1 \oplus x_2) = 8$  
    3. $S_1(x_1) = 6$ $S_1(x_2)= 2$, so $S_1(x_1) \oplus S_1(x_2) = 4  \neq S_1(x_1 \oplus x_2) = 13$  

2.  
    1. $(y_1, y_2, y_3, y_4) \rightarrow (y_2, y_1, y_4, y_3) \oplus (0,1,1,0)$  
    Row 1 from Row 0 : 
        1. $(0, 1, 1, 1) \rightarrow (1, 0, 1, 1) \oplus (0, 1, 1, 0) = (1, 1, 0, 1)$ 7 -> 13 on second row. Correct.
        2. $(1, 1, 0, 1) \rightarrow (1, 1, 1, 0) \oplus (0, 1, 1, 0) = (1, 0, 0, 0)$ 13 -> 8 on second row. Correct.
        3. $(1, 1, 1, 0) \rightarrow (1, 1, 0, 1) \oplus (0, 1, 1, 0) = (1, 0, 1, 1)$ 14 -> 11 on second row. Correct.
        4. $(0, 0, 1, 1) \rightarrow (0, 0, 1, 1) \oplus (0, 1, 1, 0) = (0, 1, 0, 1)$ 3 -> 5 on second row. Correct.
        5. $(0, 0, 0, 0) \rightarrow (0, 0, 0, 0) \oplus (0, 1, 1, 0) = (0, 1, 1, 0)$ 0 -> 6 on second row. Correct.
    2.  
        1. Row 3: $(1, 0, 1, 0) \rightarrow (0, 1, 0, 1) \oplus (0, 1, 1, 0) = (0, 0, 1, 1)$ 10 -> 3 on second row. Correct.  
                  $(0, 1, 1, 0) \rightarrow (1, 0, 0, 1) \oplus (0, 1, 1, 0) = (1, 1, 1, 1)$ 6 -> 15 on second row. Correct.  

3.  
    1. Consider the example sequence of bits 10001:  
        $x_1 \rightarrow  IP(x) = y = x_{58}$ and $IP^{-1}(y) = x_1$  
        $x_2 \rightarrow  IP(x) = y = x_{50}$ and $IP^{-1}(y) = x_2$  
        $x_3 \rightarrow  IP(x) = y = x_{42}$ and $IP^{-1}(y) = x_3$  
        $x_4 \rightarrow  IP(x) = y = x_{34}$ and $IP^{-1}(y) = x_4$  
        $x_5 \rightarrow IP(x) = y = x_{26}$ and $IP^{-1}(y) = x_5$  

4.  
    Initial plaintext: 0x0000000000000000  
    Initial key: 0x0000000000000000  
    Permutation: doesn't change anything 
    Expansion: only adds zeros  
    Output of the S-boxes: 1101 1111 1010 0111 0010 1100 0100 1101 (EFA72C4D)  
    After the permutation: 1101 1000 1101 0011 0110 1111 1101 1000 (D8D36FD8) 
    $R_1 = L_0 \oplus f(R_0, K_1)$  
    Output = $L_1R_1= 0000000 D8D36FD8$  

5.  
    Initial plaintext: 0xFFFFFFFFFFFFFFFF  
    Initial key: 0xFFFFFFFFFFFFFFFF
    Permutation: doesn't change anything  
    Expansion: only adds ones
    XOR with key = $1 \oplus 1 = 0$, output is all zeroes  
    Output of the S-boxes: 1101 1111 1010 0111 0010 1100 0100 1101 (EFA72C4D)  
    After the permutation: 1101 1000 1101 0011 0110 1111 1101 1000 (D8D36FD8)  
    $R_1 = L_0 \oplus f(R_0, K_1)$  
    Output = $L_1R_1= FFFFFFFF D8D36FD8$  

6.  
    1.  
    Initial plaintext: 0x0200000000000000   
    Initial key: 0x0000000000000000
    Permutation: 0x0000000000000001
    Expansion: 32 bits from the right, so 0x00000001, after expansion: 0x800000000002
    XOR with key = output doesn't change  -> 8 6-bit blocks: 100000 000000 000000 000000 000000 000010
    Output of the S-boxes: 0100 1111 1010 0111 0010 1100 0100 0010(4FA72C42)  
    After the permutation: 1101 0001 0101 1010 0101 0010 0101 1000(D1595298)
    $R_1 = L_0 \oplus f(R_0, K_1)$  
    Output = $L_1R_1= 0x00000000 D1595298$  
    2 S-boxes changed value, the first and the last ones.
    2. According to the design criteria for S-boxes, if two inputs differ in one bit, their outputs must differ in at least 2 bits.
    3. Output = $L_1R_1= 0x00000000 D1595298$  
    4. 4 output bits changed, confirming the design criteria.  

7.  1. Key bit at position 1 is flipped before PC-1, after PC-1 it becomes the 8th output bit and goes into C0. Now every round subkey is built by shifting C,D, and applying PC-2. As the bit 1 is in c0, its effect propagates into some subkey bits, so it should change some positions for almost every round key:  
    Round 1: C position 7, PC-2 20, subkey 19-24, S-box 4  
    Round 2: C position 6, PC-2 10, subkey 7-12, S-box 2  
    Round 3: C position 4, PC-2 16, subkey 13-18, S-box 3  
    Round 4: C position 2, PC-2 24, subkey 19-24, S-box 4  
    Round 5: C position 28, PC-2 8, subkey 7-12, S-box 2  
    Round 6: C position 26, PC-2 17, subkey 13-18, S-box 3  
    Round 7: C position 24, PC-2 4, subkey 1-6, S-box 1  
    Round 8: C position 22, PC-2 -, -, -  
    Round 9: C position 21, PC-2 11, subkey 7-12, S-box 2  
    Round 10: C position 19, PC-2 14, subkey 13-18, S-box 3  
    Round 11: C position 17, PC-2 2, subkey 1-6, S-box 1   
    Round 12: C position 15, PC-2 9, subkey 7-12, S-box 2  
    Round 13: C position 13, PC-2 , -, -  
    Round 14: C position 11, PC-2 3, subkey 1-6, S-box 1  
    Round 15: C position 9, PC-2 -, -, -  
    Round 16: C position 8, PC-2 18, subkey 13-18, S-box 3  
    2.  
    Round 1: C position 8, PC-2 18, subkey 13-18, S-box 3  
    Round 2: C position 9, PC-2 -, -, -  
    Round 3: C position 11, PC-2 3, subkey 1-6, S-box 1    
    Round 4: C position 13, PC-2 , -, -  
    Round 5: C position 15, PC-2 9, subkey 7-12, S-box 2  
    Round 6: C position 17, PC-2 2, subkey 1-6, S-box 1  
    Round 7: C position 19, PC-2 14, subkey 13-18, S-box 3   
    Round 8: C position 21, PC-2 11, subkey 7-12, S-box 2  
    Round 9: C position 22, PC-2 -, -, -  
    Round 10: C position 24, PC-2 4, subkey 1-6, S-box 1  
    Round 11: C position 26, PC-2 17, subkey 13-18, S-box 3   
    Round 12: C position 28, PC-2 8, subkey 7-12, S-box 2  
    Round 13: C position 2, PC-2 24, subkey 19-24, S-box 4  
    Round 14: C position 4, PC-2 16, subkey 13-18, S-box 3  
    Round 15: C position 6, PC-2 10, subkey 7-12, S-box 2  
    Round 16: C position 7, PC-2 20, subkey 19-24, S-box 4  
    The outputs are mirrored.  

8.  
    1. Starting backwards, k1's first 2 bits are bits 14 and 17 from before PC-2. 14 and 17 are the result of the right shift, so to unshift them we get 2 and 14. On the PC-1 2 and 14 were 49 and 18. Therefore, the first two bits are directly connected to the bits 49 and 18.  
    2. Repeating the same procedure, k2's 14 and 17 -> 2 and 14. 2 and 14 from C1 D1, so we shift them again and get 13 and 2. Those are related to 49 and 26 from the table before PC-1. Therefore, the first two bits of k2 are directly connected to the bits 49 and 26.  

9.  
    1.  In order for encryption and decryption to be the same operations, we need all keys to be equal.
    2.  0x0101010101010101  
        0xFEFEFEFEFEFEFEFE  
        0x1F1F1F1F0E0E0E0E  
        0xE0E0E0E0F1F1F1F1   
        All these have symmetrical patterns, that when shifted, will end up with the same pattern. So we will have the same blocks going into the S-boxes everytime, for example.
    3.  $2^2 / 2^{56} = 1 in 2^{54} of being a weak key$  

10.  
    1. A' = x | x does not belong to A. XOR is equivalent to $(A \cup B) - (A \cap B)$, the symmetric equivalence. With a truth table, we can see A xor B will be equal to A' xor B' only when A = B and A' = B'. For the second operation, A' xor B = (A xor B)'. With a truth table we can prove it as true.
    2. 0x00000000000001, complement should be 0xFFFFFFFFFFFFFE. Going through PC-1 should result in 0xFF7FFFFFFFFFFF. PC-1 with the original number results in 0x00800000000000. 0xFF7FFFFFFFFFFF.
    3. Proof by counterexample: Ci-1 = 1010, C'i-1 = 0101. Left Shift of Ci-1 = 0101. Complement of the left shift of Ci-1 = 1010. Left shift of C'i-1 = 1010. There is no counterexample, as the left shift only "moves", it keeps the exact same pattern of zeros and ones, which should be the exact same as the complement.
    4.  Ki = PC-2(LS1(PC-1(k))). K'i = PC-2(LS1(PC-1(k)))'. Substituing with what we know, we get K'i = PC-2(LS1(PC-1(k))') = PC-2(LS1(PC-1(k')))
    5. IP(x') = (IP(x))'. X = 0000000000000001. X' = FFFFFFFFFFFFFFFE = . IP(x) = 0000008000000000. IP(x)'= FFFFFF7FFFFFFFFF. IP(x') = FFFFFF7FFFFFFFFF. At the end the same bit goes to the same place in both  
    6. E(R'i) = (E(Ri))' = Ri = 00000001. E(Ri) = 800000000002. R'i = FFFFFFFE. E(R'i) = 7FFFFFFFFFFD. E(Ri)' = 7FFFFFFFFFFD.   
    7. Analyzing the Feistel function:  
        1. Expansion. Proven in 6.
        2. Key XOR. E(R'i) XOR K'i= (E(Ri))' XOR K'i. With A' XOR B' = A XOR B, we know:  E'(Ri) XOR K'i= E(Ri) XOR Ki
        3. S-boxes and IP: Using 3, we know E(R'i-1) XOR k'i = E(Ri-1)XOR ki. f(R'1,K'i) = f(Ri-1, Ki)
        4. R' = L'i-1 XOR f(R'i-1, K'i), R' = L'i-1 XOR f(Ri-1, Ki). Using A' XOR B = (A XOR B)', we have: R'i = (Li-1 XOR f(Ri-1, Ki))' = L'i-1 XOR f(R_1, Ki). The formula for L'i should be L'i = R'i-1, complementing. So we can conclude that:  
        L'i = R'i-1 and R'i = L'i-1 XOR f(R'i-1, K'i), so every output, for each round, should be a complement of the output of the non-complement side, up until the final ciphertext, that should be a complement of the original.

11.  Straightforward: 2^56. Average: 2^28

12.  1. r/4 Hz  
     2. 1 GBps = 250 Mhz 8 GBps =  2 Ghz  

13. 1. 20 x 16 = 120 FGPAs. 100 Mhz. 12 Ghz = 12 billion encryptions. 1 COPACOBANA = 1.2 *10^9. 60,047,995,031,606,613,333,333,333.333333
    2. $2^{56}/3600$ = 10 Billions. 9 Machines  
    3. Because key searches work by exhaustive search  

14. 1. 256^8 = 1.84 * 10^19 / 10^6 = 1.84*10^13 = 528992 years  
    2. 128^8 = 7.21* 10^16 / 10^6 = 7.21*10^10 = 2286 years  
    3. 26^8 = 2088*10^9/10^6 = 2.42 days  

15.  1. BBBB 5555 5555 EEEE. BBBB 5555 5555 EEEE. 8888 0000 0000 1111. F000 0000 0000 000F.
     2. EFFF F666 6AAA AAAA BCCC. 1FFF F666 6AAA AAAA BCCC. 1FFF F666 6AAA AAAA BCCC. 1FFF F666 6AAA AAAB.


