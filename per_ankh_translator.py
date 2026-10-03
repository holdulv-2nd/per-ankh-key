#!/usr/bin/env python3
"""
Per-Ankh Key Translator
A deterministic translation engine for the Voynich Manuscript (Beinecke MS 408)
based on the Cyrillic-Slavic shorthand hypothesis.
"""

# Master Mapping Database: Voynich EVA glyphs to Early Cyrillic equivalents
PER_ANKH_DATABASE = {
    '7': 'З', 'o': 'О', '8': 'В', 'c': 'С', 'm': 'М', 'e': 'Е', 'q': 'Г',
    '9': 'Ц', 'y': 'И', 't': 'Т', 'p': 'П', 'k': 'К', 'd': 'Д', 'g': 'Ч',
    'r': 'Р', 'n': 'Н', 'a': 'А', 'h': 'Х', 's': 'С', 'l': 'Л', 'i': 'И',
    'j': 'Й', 'f': 'Ф', 'w': 'Ш', 'x': 'Х', 'b': 'Б', 'v': 'В', 'z': 'З',
    'u': 'У'
}

# Standard Slavic onset consonant clusters (do not require vowel insertion)
ALLOWED_ONSETS = {"ст", "тр", "пр", "пл", "гр", "сл", "см"}

def substitute_glyphs(word):
    """Translates individual EVA glyphs into their Cyrillic equivalents."""
    cyrillic_word = ""
    for char in word.lower():
        if char in PER_ANKH_DATABASE:
            cyrillic_word += PER_ANKH_DATABASE[char]
        elif char in ['-', '{', '}', '*', '.']:
            # Preserve structural markings and punctuation
            cyrillic_word += char
        else:
            # Mark unrecognized characters for auditing
            cyrillic_word += f"[{char}]"
    return cyrillic_word

def apply_phonotactic_theorems(cyrillic_word):
    """
    Applies the Vowel-Omission Theorems to suggest where 
    ultra-short vowels (Yers: ъ/ь) should be restored.
    """
    if not cyrillic_word or cyrillic_word.startswith('{'):
        return cyrillic_word
        
    restored = ""
    length = len(cyrillic_word)
    
    for i in range(length):
        restored += cyrillic_word[i]
        
        # Check if we have two adjacent consonants
        if i < length - 1:
            c1, c2 = cyrillic_word[i], cyrillic_word[i+1]
            vowels = "АОУЕИЫ"
            
            # If both are consonants and not in allowed punctuation/vowels
            if c1 not in vowels and c2 not in vowels and c1.isalpha() and c2.isalpha():
                cluster = c1 + c2
                if cluster.lower() not in ALLOWED_ONSETS:
                    # Apply Theorem 1.1: Insert soft yer (ь) or hard yer (ъ)
                    soft_consonants = "ЗМДЦ"
                    if c1 in soft_consonants:
                        restored += "ь"  # Soft yer
                    else:
                        restored += "ъ"  # Hard yer
                        
    # Apply Theorem 1.2: Word-final hard consonant yer-closure
    last_char = restored[-1]
    if last_char.isalpha() and last_char not in "АОУЕИЫьъ":
        restored += "ъ"
        
    return restored

def translate_line(line):
    """Processes an entire line of raw EVA text."""
    words = line.split()
    translated_words = []
    
    for word in words:
        # Step 1: Substitution
        substituted = substitute_glyphs(word)
        # Step 2: Vowel Restoration Suggestion
        restored = apply_phonotactic_theorems(substituted)
        translated_words.append(restored)
        
    return " ".join(translated_words)

if __name__ == "__main__":
    import sys

    print("--- Per-Ankh Key Translation Engine Loaded ---")
    
    # Simple interactive command line interface
    if len(sys.argv) > 1:
        raw_input = " ".join(sys.argv[1:])
        output = translate_line(raw_input)
        print(f"Raw Input:  {raw_input}")
        print(f"Plaintext:  {output}")
    else:
        print("Enter raw Voynich EVA text to translate (or 'exit' to quit):")
        while True:
            try:
                user_input = input("\n> ")
                if user_input.lower() == 'exit':
                    break
                if not user_input.strip():
                    continue
                result = translate_line(user_input)
                print(f"Cyrillic output: {result}")
            except (KeyboardInterrupt, EOFError):
                break
