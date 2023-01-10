import pyAesCrypt
import os
import sys


def decrypt_file(file_path, password, buffer_size=512 * 1024):
    """
    Decrypt a file using the specified password.
    The decrypted file will have the same name as the original, without the '.crp' extension.
    """
    try:
        # Decrypt the file
        pyAesCrypt.decryptFile(file_path, file_path[:-4], password, buffer_size)

        # Print the name of the decrypted file
        print("File '{}' decrypted.".format(os.path.basename(file_path)[:-4]))

        # Delete the encrypted file
        os.remove(file_path)

    except Exception as e:
        print("Error decrypting file: ", e)


def decrypt_directory(directory, password, buffer_size=512 * 1024):
    """
    Recursively walk through the specified directory and decrypt all '.crp' files found.
    """
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path) and path.endswith('.crp'):
            decrypt_file(path, password, buffer_size)
        elif os.path.isdir(path):
            decrypt_directory(path, password, buffer_size)

def main():
    # Input directory
    directory = input("Enter the directory path to decrypt: ")
    password = input("Enter the password for decryption: ")
    decrypt_directory(directory, password)
    # os.remove(str(sys.argv[0]))

if __name__ == '__main__':
    main()
