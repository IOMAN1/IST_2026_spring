def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""


    for i in range(len(plaintext)):
        c = plaintext[i]
        shift = ord(keyword[i % len(keyword)].upper()) - ord("A")
        if c.isalpha():
            start = ord("A") if c.isupper() else ord("a")
            ciphertext += chr(start + (ord(c) - start + shift) % 26)
        else:
            ciphertext += c

    
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""


    for i in range(len(ciphertext)):
        c = ciphertext[i]
        shift = ord(keyword[i % len(keyword)].upper()) - ord("A")
        if c.isalpha():
            start = ord("A") if c.isupper() else ord("a")
            plaintext += chr(start + (ord(c) - start - shift) % 26)
        else:
            plaintext += c


    return plaintext
