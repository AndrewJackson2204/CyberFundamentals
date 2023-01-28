lookup = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
          'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
          'K': 'abaab', 'L': 'ababa', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
          'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
          'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa',
          'Z': 'bbaab', ' ': ' '}


def encrypt(message, cipher):
    """Ecrypt the string according to the cipher provided."""
    # return ''.join(map(lookup.get, message))
    encrypted = []
    for letter in message:
        encrypted.append(lookup[letter])
    return ''.join(encrypted)


def decrypt(message, cipher):
    """Decrypt the string according to the cipher provided."""
    plaintext = []
    i = 0
    reverse_cipher = {v: k for k, v in cipher.items()}
    # emulating a do-while loop
    while True:
        # condition to run decryption till the last set of ciphertext
        if i < len(message) - 4:
            # extracting a set of ciphertext from the message
            substr = message[i:i + 5]
            # checking for space as the first character of the substring
            if substr[0] != ' ':
                # This statement gets us the key(plaintext) using the values(ciphertext)
                # Just the reverse of what we were doing in encrypt function
                plaintext.append(reverse_cipher[substr])
                i += 5  # to get the next set of ciphertext
            else:
                # adds space
                plaintext.append(' ')
                i += 1  # index next to the space
        else:
            break  # emulating a do-while loop

    return ''.join(plaintext)


def main():

    message = "BAABA BABAA ABBAB BAABB BBAAB BABAA"
    result = decrypt(message.lower(), lookup)
    print(result)

# Executes the main function
if __name__ == '__main__':
    main()
