while True:
    MOD = 128
    ch = int(input("Press 1 to Encrypt || Press 2 to Decrypt\n>>>"))
    if ch == 1:
        text = input("Text:")
        print("!!! THE KEY MUST BE TWO NUMBERS ONLY")
        print("          NUM1+SPACE+NUM2           \n")
        key = list(map(int ,input("Key:").rstrip().split()))

        cipher=[]
        for tx in text:
            cipher.append(chr((key[0] * ord(tx) + key[1]) %MOD))
        
        print("\n===================================")
        print("         !!! Encrypted !!!         ")
        print("text:","".join(cipher))  
        print("===================================\n")

    elif ch==2:
        text = input("Text:")
        key = list(map(int ,input("Key:").rstrip().split()))

        cipher=[]
        for tx in text:
            for inv in range(MOD):
                if (key[0] * inv)%MOD == 1: 
                    inverse = inv
            equ = inverse*(ord(tx)+MOD-key[1])%MOD
            if equ > MOD:
                equ -= MOD
                cipher.append(chr(equ))
            else:
                cipher.append(chr(equ)) 
        print("\n===================================")
        print("         !!! Decrypted !!!           ")
        print("Text:","".join(cipher))
        print("===================================\n")
