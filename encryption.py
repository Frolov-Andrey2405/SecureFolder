import pyAesCrypt
import os
import sys

def encrypt_file(file_path, password, buffer_size=512 * 1024):
    """
    Encrypt a file using the specified password.
    The encrypted file will be saved with a '.crp' extension.
    """
    try:
        # Encrypt the file
        pyAesCrypt.encryptFile(file_path, file_path + '.crp', password, buffer_size)

        # Print the name of the encrypted file
        print("File '{}' encrypted.".format(os.path.basename(file_path)))

        # Delete the original file
        os.remove(file_path)

    except Exception as e:
        print("Error encrypting file: ", e)


def encrypt_directory(directory, password, buffer_size=512 * 1024):
    """
    Recursively walk through the specified directory and encrypt all files found.
    """
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path):
            encrypt_file(path, password, buffer_size)
        elif os.path.isdir(path):
            encrypt_directory(path, password, buffer_size)


def main():
    # Input directory
    directory = input("Enter the directory path to encrypt: ")
    password = input("Enter the password for encryption: ")
    encrypt_directory(directory, password)
    # os.remove(str(sys.argv[0]))


if __name__ == '__main__':
    main()
