
def generate_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     

# for the encyption
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x = x + ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
     
# for the decryption
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x = x + ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
     

string = input("Give me A String: ").upper()
keyword = input("Give me the key: ").upper()
key = generate_key(string, keyword)
cipher_text = cipherText(string,key)
print("Ciphertext :", cipher_text)
print("Original/Decrypted Text :", originalText(cipher_text, key))