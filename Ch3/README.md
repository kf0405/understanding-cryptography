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
        $x_1 \rightarrow $ $IP(x) = y = x_58$ and $IP^{-1}(y) = x_1$  
        $x_2 \rightarrow $ $IP(x) = y = x_50$ and $IP^{-1}(y) = x_2$  
        $x_3 \rightarrow $ $IP(x) = y = x_42$ and $IP^{-1}(y) = x_3$  
        $x_4 \rightarrow $ $IP(x) = y = x_34$ and $IP^{-1}(y) = x_4$  
        $x_5 \rightarrow $ $IP(x) = y = x_26$ and $IP^{-1}(y) = x_5$  

4.  
    Initial plaintext: 0x0000000000000000  
    Initial key: 0x0000000000000000  
    Permutation: doesn't change anything 
    Expansion: only adds zeros  
    Output of the S-boxes: 1110 0100 1101 0001 0010 1111 1011 1000  (E4D12FB8)  
    After the permutation: 1111 1010 1010 1100 1000 0000 1111 0011 (FAAC80F3)  
    $R_1 = L_0 \oplus f(R_0, K_1)$  
    Output = $L_1R_1= 0000000 FAAC80F3$  

5.  
    Initial plaintext: 0xFFFFFFFFFFFFFFFF  
    Initial key: 0xFFFFFFFFFFFFFFFF
    Permutation: doesn't change anything  
    Expansion: only adds ones
    XOR with key = $1 \oplus 1 = 0, output is all zeroes$
    Output of the S-boxes: 1101 1001 1100 1110 0011 1101 1100 1011  (E4D12FB8)  
    After the permutation: 1111 1010 1010 1100 1000 0000 1111 0011 (FAAC80F3)  
    $R_1 = L_0 \oplus f(R_0, K_1)$  
    Output = $L_1R_1= FFFFFFFF FAAC80F3$  

6.  
    1.  