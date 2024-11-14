#!/usr/bin/env python3

# Ciphertext: xcqv{gvyavn_zvztv_etvtddlnxcgy}
# we have to find the plaintext

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"


def all_keys():
    for i in range(0, 26):
        key = "".join([alphabet[i:], alphabet[0 : i]])
        plain = decrypt("xcqv{gvyavn_zvztv_etvtddlnxcgy}", key)
        print(f"\n\n{key}\t\t{plain}\n")
        for j in range(0, 26):
            key2 = "".join([alphabet[j:], alphabet[0 : j]])
            chyper = encrypt(plain, key2)
            print(f"{key2}\t{chyper}")

def generateKey():
    start = random.randint(1, 25)
    key = "".join([alphabet[start:], alphabet[0:start]])
    return key


def encrypt(plain, key):
    ciphertext = ""
    for k in range(len(plain)):
        character = plain[k]

        if ord(character) <= 90 and ord(character) >= 65:
            i = alphabet.index(chr(ord(character) + 32))        # convert to lowercase and get position in alphabet
            characterEncrypted = chr(ord(key[i]) - 32)          # take the i character from key and converto to uppercase
            key = "".join([key[len(key) - 1 :], key[0 : len(key) - 1]])         # shift left key ["1234" --> "4123"]
            ciphertext = "".join([ciphertext, characterEncrypted])      # append to string
        elif ord(character) <= 122 and ord(character) >= 97:
            i = alphabet.index(character)
            characterEncrypted = key[i]
            key = "".join([key[len(key) - 1 :], key[0 : len(key) - 1]])
            ciphertext = "".join([ciphertext, characterEncrypted])
        else:
            ciphertext = "".join([ciphertext, character])

    return ciphertext

# def decrypt(chyper, key):
#     plain = ""
#     for k in range(len(chyper)):
#         if chyper[k].isalpha():
#             key = "".join([key[1:], key[0]])        # shift rigth key ["1234" --> "2341"]
#             i = key.index(chyper[k])
#             char = alphabet[i]
#             plain += char
#         else:
#             plain += chyper[k]
#     return plain


def decrypt(ciphertext, key):
    plaintext = ""
    
    # Itera su ogni carattere nel testo cifrato
    for k in range(len(ciphertext)):
        character = ciphertext[k]

        # Verifica se il carattere è una lettera maiuscola
        if ord(character) <= 90 and ord(character) >= 65:
            # Trova la posizione del carattere cifrato nella chiave, convertendolo in minuscolo
            i = key.index(chr(ord(character) + 32))
            # Ottieni la lettera dell'alfabeto originale corrispondente (in maiuscolo)
            characterDecrypted = chr(ord('a') + i).upper()
            # Ripristina la chiave al passo precedente (rotazione inversa)
            key = "".join([key[1:], key[0]])
            # Aggiungi il carattere decifrato al testo in chiaro
            plaintext = "".join([plaintext, characterDecrypted])
        
        # Verifica se il carattere è una lettera minuscola
        elif ord(character) <= 122 and ord(character) >= 97:
            # Trova la posizione del carattere cifrato nella chiave
            i = key.index(character)
            # Ottieni la lettera dell'alfabeto originale corrispondente
            characterDecrypted = chr(ord('a') + i)
            # Ripristina la chiave al passo precedente (rotazione inversa)
            key = "".join([key[1:], key[0]])
            # Aggiungi il carattere decifrato al testo in chiaro
            plaintext = "".join([plaintext, characterDecrypted])
        
        # Mantieni i caratteri non alfabetici inalterati
        else:
            plaintext = "".join([plaintext, character])

    return plaintext



def handle():
    plaintextFLAG = "xbos{cqstne_pkngh_pdebkjqraehy}"
    key = generateKey()
    ciphertext = encrypt(plaintextFLAG, key)
    print(ciphertext)

    return


if __name__ == "__main__":
    print(f"key\t\tplain\t\tchyper\n\n")
    all_keys()
 
    # handle()