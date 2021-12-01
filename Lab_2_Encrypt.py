def encrypt(key, message):
    message = message.upper()
    alphabet = 'ABCDEFGHIJKMLNOPQRSTUVWXYZ'
    result = ''

    for letter in message:
        if letter in alphabet:  # if the letter is actually a letter
            # encrypt it
            # find the corresponding ciphertext letter in the alphabet
            letter_index = (alphabet.find(letter) + key) % len(alphabet)

            result += alphabet[letter_index]

        else:
            result = result + letter

    return result


def decrypt(key, message):
    message = message.upper()
    alphabet = 'ABCDEFGHIJKMLNOPQRSTUVWXYZ'
    result = ''

    for letter in message:
        if letter in alphabet:  # if the letter is actually a letter
            # encrypt it
            # find the corresponding ciphertext letter in the alphabetbet
            letter_index = (alphabet.find(letter) - key) % len(alphabet)

            result += alphabet[letter_index]

        else:
            result = result + letter

    return result

# Main function that uses both encrypt and decrypt functions to create an encrypted file using the Caesar cypher


def main():
    user_message = input(
        "Input a long text and press ENTER once you're done: ")
    user_key = input(
        "Input a number from 0-25 for your key and press ENTER once you're done: ")
    file_key = open('key.txt', 'w')
    file_key.write(user_key)
    file_key.close()

    user_key = int(user_key)
    encrypted_message = encrypt(user_key, user_message)

    # Write in file key and message
    file_message = open('message.txt', 'w')
    file_message.write(encrypted_message)
    file_message.close()


if __name__ == "__main__":
    main()
