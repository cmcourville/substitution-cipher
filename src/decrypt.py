def get_letter_frequency(cipher_text: str) -> dict:
    """
    Get the frequency of each letter in the cipher text.
    Only counts letters in the English alphabet (A-Z, a-z).
    """
    frequency = {}
    for letter in cipher_text:
        # Check if the letter is in the English alphabet (case insensitive)
        if letter.isalpha():
            # Convert to uppercase for consistent counting
            letter_upper = letter.upper()
            if letter_upper in frequency:
                frequency[letter_upper] += 1
            else:
                frequency[letter_upper] = 1
    return sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

def map_cipher_to_english_frequency(sorted_cipher_frequency: list) -> dict:
    """
    Map the sorted cipher letters to English letter frequency data.
    Maps the most frequent cipher letter to the most frequent English letter (E), etc.
    
    Args:
        sorted_cipher_frequency: List of tuples (cipher_letter, count) sorted by frequency
        
    Returns:
        dict: Dictionary mapping cipher letters to likely English letters
    """
    from english_letter_frequency import ENGLISH_LETTER_FREQUENCY_SORTED_V2 as ENGLISH_LETTER_FREQUENCY
    
    # Create mapping dictionary
    cipher_to_english = {}
    
    # Map each cipher letter to the corresponding English letter by frequency rank
    for i, (cipher_letter, count) in enumerate(sorted_cipher_frequency):
        if i < len(ENGLISH_LETTER_FREQUENCY):
            english_letter = ENGLISH_LETTER_FREQUENCY[i][0]
            cipher_to_english[cipher_letter] = english_letter
    print(cipher_to_english)
    return cipher_to_english


def replace_letters(cipher_text: str, replacement_dict: dict) -> str:
    """
    Replace the letters in the cipher text with the replacement letters.
    Handles both uppercase and lowercase letters.
    """
    result = ""
    for char in cipher_text:
        if char.isalpha():
            # Convert to uppercase for mapping lookup
            char_upper = char.upper()
            if char_upper in replacement_dict:
                # Replace with the mapped letter, preserving original case
                replacement = replacement_dict[char_upper]
                if char.islower():
                    result += replacement.lower()
                else:
                    result += replacement
            else:
                result += char  # Keep original character if not in mapping
        else:
            result += char  # Keep non-alphabetic characters as-is
    return result

def decrypt_and_save_to_file(cipher_text: str, output_file: str) -> str:
    """
    Decrypt the cipher text using frequency analysis and save to file.
    
    Args:
        cipher_text: The encrypted text to decrypt
        output_file: Path to the output file (default: ../plaintext.txt)
        
    Returns:
        str: The decrypted text
    """
    # Get frequency analysis
    sorted_frequency = get_letter_frequency(cipher_text)
    print(sorted_frequency)
    
    # Map cipher letters to English letters
    mapping = map_cipher_to_english_frequency(sorted_frequency)
    
    # Replace letters in the cipher text
    decrypted_text = replace_letters(cipher_text, mapping)
    
    # Write to file
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decrypted_text)
        print(f"Decrypted text saved to {output_file}")
    except Exception as e:
        print(f"Error writing to file: {e}")
    
    return decrypted_text