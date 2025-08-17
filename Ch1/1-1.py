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

with open("cipher.txt", "r") as f:
    cipher = f.read()


plaintext = decrypt(cipher)
'''
Current plaintext:
GEUAFSE TRE YHAUTNUE IC TRE GASNU MIVEMEOTS IC PATA NS
TRE CIUFS AOD MASTEHW IC SELC NS TRE ESSEOUE IC
MATSFGAWASRN HWF PAHATE DI N SRALL THW TI ELFUNDATE TRE
MIVEMEOTS IC TRE PATA AUUIHDNOB TI MW NOTEHYHETATNIO
GASED IO CIHTW WEAHS IC STFDW

NT NS OIT AO EASW TASP TI EKYLANO EAUR MIVEMEOT AOD NTS
SNBONCNUAOUE AOD SIME MFST HEMANO FOEKYLANOED TI BNVE A
UIMYLETE EKYLAOATNIO IOE XIFLD RAVE TI GE QFALNCNED AOD
NOSYNHED TI SFUR AO EKTEOT TRAT RE UIFLD HEAUR TRE STATE
IC EOLNBRTEOED MNOD UAYAGLE IC HEUIBONJNOB SIFODLESS
SIFOD AOD SRAYELESS SRAYE N DI OIT DEEM MWSELC TRE CNOAL
AFTRIHNTW GFT MW EKYEHNEOUE XNTR PATA RAS LECT OI DIFGT
TRAT TRE CILLIXNOB NS TRE YHIYEH AYYLNUATNIO AOD
NOTEHYHETATNIO N ICCEH MW TREIHNES NO TRE RIYE TRAT TRE
ESSEOUE IC IPNOAXAO PAHATE XNLL HEMANO NOTAUT

Will atempt to exchange letters manually until we find a solution
'''
correct_key = [
        ('r', 'E'),('m', 'A'), ('i', 'S'), ('b', 'T'), ('c','W'),
        ('w', 'I'), ('k', 'N'), ('j', 'O'), ('l', 'B'), ('v', 'C'),
        ('n', 'U'), ('t', 'Y'), ('q', 'K'), ('s', 'P'), ('p', 'H'),
        ('a', 'X'), ('u', 'R'), ('y', 'M'), ('x', 'F'), ('h', 'L'),
        ('o', 'G'), ('e', 'V'), ('d', 'D'), ('g', 'Z')
    ]

plaintext_2 = manual_decrypt(cipher, correct_key)
print(plaintext_2)

'''
BECAUSE THE PRACTICE OF THE BASIC MOVEMENTS OF KATA IS
THE FOCUS AND MASTERY OF SELF IS THE ESSENCE OF
MATSUBAYASHI RYU KARATE DO I SHALL TRY TO ELUCIDATE THE
MOVEMENTS OF THE KATA ACCORDING TO MY INTERPRETATION
BASED ON FORTY YEARS OF STUDY

IT IS NOT AN EASY TASK TO EXPLAIN EACH MOVEMENT AND ITS
SIGNIFICANCE AND SOME MUST REMAIN UNEXPLAINED TO GIVE A
COMPLETE EXPLANATION ONE WOULD HAVE TO BE fUALIFIED AND
INSPIRED TO SUCH AN EXTENT THAT HE COULD REACH THE STATE
OF ENLIGHTENED MIND CAPABLE OF RECOGNIZING SOUNDLESS
SOUND AND SHAPELESS SHAPE I DO NOT DEEM MYSELF THE FINAL
AUTHORITY BUT MY EXPERIENCE WITH KATA HAS LEFT NO DOUBT
THAT THE FOLLOWING IS THE PROPER APPLICATION AND
INTERPRETATION I OFFER MY THEORIES IN THE HOPE THAT THE
ESSENCE OF OKINAWAN KARATE WILL REMAIN INTACT
Result of the brute force
Analysis: Statistical approach may have shown a few similarities, but it is clearly not enough, and many manual alterations had to be done for it to work
'''