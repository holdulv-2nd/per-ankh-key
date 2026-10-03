# The Per-Ankh Key: Cyrillic-Slavic Decipherment of the Voynich Manuscript

This repository houses the open-source implementation of the **Per-Ankh Key**, a deterministic visual-phonetic translation framework designed to decode the Voynich Manuscript (Beinecke MS 408).

## The Hypothesis
The Voynich Manuscript is proposed to be a medieval herbalist's manual written in a stylized, cursive, and ligatured shorthand of the early Cyrillic alphabet, spelling out Middle Slavic and Old Church Slavonic roots.

## The Mathematical Framework
Rather than relying on intuitive, ad-hoc vowel insertions, this project uses a three-layer cryptosystem:
1. **The Static Mapping Database:** A fixed glyph-to-letter translation table.
2. **The Phonotactic Vowel Theorem:** A deterministic algorithm for restoring short vowels (Yers: ъ/ь) based on standard Slavic onset rules.
3. **The Ligature Decomposition Matrix:** Strict geometric rules for expanding fused characters.

## How to Test
1. Clone this repository.
2. Run `per_ankh_translator.py`.
3. Input any raw EVA transcription string to view the mathematical Cyrillic output.
4. We invite cryptographers, linguists, and historians to audit these outputs against the physical illustrations.
