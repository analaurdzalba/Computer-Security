import Lab_2_Encrypt as e


def main():
    encrypted_message = open("message.txt", "r")
    message = encrypted_message.readlines()
    encrypted_message.close()

    file_key = open("key.txt", "r")
    key = file_key.readlines()
    file_key.close()

    key = int(key[0])
    message = str(message[0])
    decrypted_message = e.decrypt(key, message)
    file = open("decrypted_message.txt", "w")
    file.write(decrypted_message)
    file.close()


if __name__ == "__main__":
    main()
