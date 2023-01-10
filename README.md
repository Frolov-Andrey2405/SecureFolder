# SecureFolder 🔒
This code is a Python🐍 script that encrypts all the files in a specified directory, including files in subdirectories. The script uses the pyAesCrypt library to handle the encryption and the os library to interact with the file system. The script also uses sys library to remove the script file after running the script.

### The script is divided into three main functions:
- **encrypt_file(file_path, password, buffer_size=512 * 1024): 🔒**
This function takes in a file path and a password as input. It uses the pyAesCrypt.encryptFile() method to encrypt the file and save it with a '.crp' extension. It also prints the name of the encrypted file and deletes the original file.
- **encrypt_directory(directory, password, buffer_size=512 * 1024): 🗂️** 
This function takes in a directory path and a password as input. It uses the os.listdir() function to get a list of all files and subdirectories in the specified directory. It then uses the encrypt_file() function to encrypt all files and recursively calls itself to encrypt files in subdirectories.

- **main(): 🔑**
This function prompts the user to input the directory path and password to be used for encryption. It then calls the encrypt_directory() function to encrypt all files in the specified directory.

#### Technologies and Libraries 🛠️
- **[Python 3.x+](https://www.python.org/)**
- **[pyAesCrypt](https://pypi.org/project/pyAesCrypt/)**