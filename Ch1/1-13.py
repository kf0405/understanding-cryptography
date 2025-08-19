ptext = ''
a_1 = 15
b = 22
m = 26
with open("cipher1-13.txt", "r") as f:
    cipher = f.read()
for letter in cipher:
    charval = (a_1*(ord(letter)-97-b)) % m
    ptext += chr(charval+97) # 97 is a btw and charval its converted value
print(ptext)
'firstthesentenceandthentheevidencesaidthequeen is the answer'