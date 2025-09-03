import os
from decrypt import decrypt_and_save_to_file


def read_cipher_file():
    """
    Reads the cipher.txt file and returns its contents as a string.
    
    Returns:
        str: The contents of the cipher.txt file
    """
    try:
        with open('cipher.txt', 'r', encoding='utf-8') as file:
            cipher_text = file.read()
        return cipher_text
    except FileNotFoundError:
        print("Error: cipher.txt file not found")
        return None
    except Exception as e:
        print(f"Error reading cipher.txt: {e}")
        return None


if __name__ == "__main__":
    # Print current directory
    print(f"Current directory: {os.getcwd()}")
    
    # Example usage
    cipher_content = read_cipher_file()
    if cipher_content:
        decrypted_text = decrypt_and_save_to_file(cipher_content, 'plaintext.txt')
        print("Decryption complete!")








