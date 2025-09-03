# English letter frequency data (based on analysis of large text corpora)
# Values represent the percentage frequency of each letter in typical English text
ENGLISH_LETTER_FREQUENCY = {
    'E': 12.02,  # Most common letter
    'T': 9.10,
    'A': 8.12,
    'O': 7.68,
    'I': 6.97,
    'N': 6.95,
    'S': 6.28,
    'H': 6.09,
    'R': 5.99,
    'D': 4.25,
    'L': 4.03,
    'C': 2.78,
    'U': 2.76,
    'M': 2.41,
    'W': 2.36,
    'F': 2.23,
    'G': 2.02,
    'Y': 1.97,
    'P': 1.93,
    'B': 1.29,
    'V': 0.98,
    'K': 0.77,
    'J': 0.15,
    'X': 0.15,
    'Q': 0.10,
    'Z': 0.07
}

# Alternative format: sorted by frequency (most common first)
ENGLISH_LETTER_FREQUENCY_SORTED = [
    ('E', 12.02), ('T', 9.10), ('A', 8.12), ('O', 7.68), ('I', 6.97),
    ('N', 6.95), ('S', 6.28), ('H', 6.09), ('R', 5.99), ('D', 4.25),
    ('L', 4.03), ('C', 2.78), ('U', 2.76), ('M', 2.41), ('W', 2.36),
    ('F', 2.23), ('G', 2.02), ('Y', 1.97), ('P', 1.93), ('B', 1.29),
    ('V', 0.98), ('K', 0.77), ('J', 0.15), ('X', 0.15), ('Q', 0.10), ('Z', 0.07)
]

# Most common bigrams (two-letter combinations) in English
ENGLISH_BIGRAM_FREQUENCY = {
    'TH': 3.56, 'HE': 3.07, 'IN': 2.43, 'ER': 2.05, 'AN': 1.99,
    'RE': 1.85, 'ND': 1.78, 'ON': 1.76, 'EN': 1.69, 'AT': 1.68,
    'OU': 1.54, 'ED': 1.49, 'HA': 1.47, 'TO': 1.45, 'OR': 1.38,
    'IT': 1.33, 'IS': 1.32, 'HI': 1.28, 'ES': 1.26, 'NG': 1.20
}

# Most common trigrams (three-letter combinations) in English
ENGLISH_TRIGRAM_FREQUENCY = {
    'THE': 1.81, 'AND': 0.73, 'ING': 0.72, 'ENT': 0.42, 'ION': 0.42,
    'HER': 0.36, 'FOR': 0.34, 'THA': 0.33, 'NTH': 0.33, 'INT': 0.32,
    'ERE': 0.31, 'TIO': 0.31, 'TER': 0.30, 'EST': 0.28, 'ERS': 0.28
}

def get_english_frequency_data():
    """
    Returns a dictionary containing all English frequency data.
    
    Returns:
        dict: Dictionary with keys 'letters', 'letters_sorted', 'bigrams', 'trigrams'
    """
    return {
        'letters': ENGLISH_LETTER_FREQUENCY,
        'letters_sorted': ENGLISH_LETTER_FREQUENCY_SORTED,
        'bigrams': ENGLISH_BIGRAM_FREQUENCY,
        'trigrams': ENGLISH_TRIGRAM_FREQUENCY
    }

def print_frequency_data():
    """
    Prints the English frequency data in a readable format.
    """
    print("English Letter Frequency (percentage):")
    print("-" * 40)
    for letter, freq in ENGLISH_LETTER_FREQUENCY_SORTED:
        print(f"{letter}: {freq:5.2f}%")
    
    print("\nMost Common Bigrams:")
    print("-" * 20)
    for bigram, freq in list(ENGLISH_BIGRAM_FREQUENCY.items())[:10]:
        print(f"{bigram}: {freq:4.2f}%")
    
    print("\nMost Common Trigrams:")
    print("-" * 20)
    for trigram, freq in list(ENGLISH_TRIGRAM_FREQUENCY.items())[:10]:
        print(f"{trigram}: {freq:4.2f}%")

if __name__ == "__main__":
    print_frequency_data()
