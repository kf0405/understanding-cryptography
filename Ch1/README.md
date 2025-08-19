# Problems

1. 
    1. Solution in 1-1.py
    2. Solution in 1-1.py
    3. Shoshin Nagamine  

2. 
    1. Solution in 1-2.py
    2. Tecumseh  

3. 
    1. 2^128 = 10^38.53 base 10. 1 million = 10000 ASICs(due to overhead). 10000 x 5 x (10^8) = 5 x 10^12 keys per second.10^38.53 / 5 10^12 = 5 x 10^28 seconds = 1.58 x 10^21 years. Therefore the time it takes is more than 10^11 times than the age of the universe 10^10.
    2. Considering Moore's Law is already no longer valid: 1.58 x 10 ^21 x 365/2^i = 1 day. 2^i = 1.58 x 10^21 x 365 = 2^i. i = 77.93 = 78 (Number of Moore iterations). 78 * 1.5(Iteration length) = 117 years.  

4. 
    1. 5764801 = $7^8$
    2. $2^23$ keylength of 23 bits
    3. 26 lowercase letters, but all of the ascii lowercase letters go from 97 to 122, so we need 128, 7 bits.
    4. 1 character for both  

5.  
    1. $2^64$
    2. $(2^64+2^63+...+2+1)*0.03$. $2^64$ by itself is already bigger than $10^19$, which is almost $10^10$ times the worldwide yield
    3. 102.4 mm
    4. 20 times
    5. 29 times is 536,870Km
    6. 73 times is $9.44*10^21$ so 74 times  

6.  
    1. no, yes, yes, no, yes, no
    2. no, no, no, no, no, no  

7.  
    1. All result in 6

8. 
    1. 1/5
    2. 1/5
    3. 6/5

9. 
   4. For Z4, we have 1 and 3 and for Z6, 1 and 5 are the only ones with an inverse, the others don't have. As 5 is prime, all elements will have an inverse in its ring.

10. 
    1. 11 is prime - every number will have an inverse. For 5, we have 9
    2. 12 is not prime - 5 has inverse in 5, as 25 is 1 mod 12
    3. 13 is prime - 5 * 8 = 40 = 1 mod 13.

11. 
    1. 9 mod 13 is 9
    2. 49 mod 13 is 10
    3. $3^10$ mod 13 is the same as $3^4*3^4*3^2$. We get $3*3*9$ mod 13, and the final result is 3
    4. $7^100$ mod 13 -> we have to use Fermat's little Theorem. 13 is prime and 7 is not divisible by it, so we can find that $7^13-1$ will be 1 mod 13. So we have to reduce 100 to multiples of 12. $7^12*8 * 7^4$ is our final reduction. With that, only $7^4 will remain in the end$. $49 mod 13$ is 10, so we have 100 mod 13, whose result is 9.
    5. $7^x\equiv 11 \mod 13$ ->  we can find values by trying for the first few integers. We'll find success with 5. 7 has order 12 for mod 13 (Fermat), so the result of all possible x's will be $5 + 12*k for any integer.
    Note on Fermat: if a number has a certain order, that means $7^x+12 \equiv 7^x$  

12.  
    1. Euler's phi for 4, 5, 9, 26: 2, 4, 6, 12. So, if a number is prime, its Euler phi function will result in it - 1. If it is not prime and is a perfect square, it will be itself minus its square root. If it is a coprime, it will be the multiplication of the phi of its divisors.  

13.  
    1. We decrypt it by using the decryption expression for affine ciphers, $d= x \equiv a^{-1}*(y-b)\mod 26$ with a as 7 and b as 22. The inverse of a for Z26 is 15. The rest will be solved with the code in 1-13.py. 
    2. The result is a quote from Alice in Wonderland by Lewis Carrol.

14.  
    1. $d= x \equiv a^{-1}*(y-b)mod29$ and $e= x \equiv (a*x+b)mod29$. As m is prime, all numbers from a to 28 are possible a's.
    2. A key in the affine cipher is the pair (a,b). Where b is the Euler phi of a. For a = 29, we should have b = 28. 29 * 28 = 812 possible keys
    3. The letters correspond to the values $26, 20, 29, 22, 29$. Using the decrypt function from 1, considering the inverse of 17 is 23 for 30,  we can obtain the result of: Frodo.
    4. From the shire  

15.  
    With two pairs of plaintext and ciphertext, we can make a system, where $y_{1}\equiv (a*x_{1}+b) \mod m$ and $y_{2}\equiv (a*x_{2}+b) \mod m$.
    With the two pairs we will only have to find the values of a and b, which should be trivial.  

16. 
    1. $e_{k2}\equiv a_2*(a_1*x_1 + b_1) + b2 \mod 26$. X here is an encrypted x itself. The keyspace of one function doesn't depend on the other, but only on its a, b and m. Considering the result of the affine cipher is always another letter in the alphabet, x will just be a valid letter for $e_{k2}$, so there could easily be a V$e_{k3}\equiv a_3*x + b3 \mod 26$.
    2. $a_3=33$, $b_3\eq62$.
    3. With $e_{k3}$ we get 9 or I, with $e_{k1}$ and then $e_{k2}$ we also get 9 or I.
    4. The effective key space is not altered, as we still use the same m, and m is the value that matters for obtaining the keyspace.  

17.  
    1. $k = 9, 0, 12, 0, 8, 10, 0$
    2. $k = 9, 0, 12, 0, 8, 10, 0, 9, 0, 12, 0, 8$. Codebreakers then becomes "LOPEJBEJKQRA".
    3. In a known-plaintext attack, one could try matching a sequence of letters until they could find the size of the key and the key itself. The cipher should eventually generate repeated sequences too, so it should be exploitable using that. 
