# Vowel-Omission Theorem (Phonotactics)

This document details the first mathematical layer of the **Per-Ankh Key**: the deterministic rules for restoring omitted vowels (Yers) from consonant clusters in the Voynich Manuscript.

## 1. The Historical Linguistic Basis
Medieval Slavic (such as Old Church Slavonic) was governed by the **Law of Open Syllables**, meaning syllables had to end in a vowel sound. The language featured two ultra-short, weak vowels known as **Yers**:
* **ъ** (Hard Yer / short back vowel, vocalizing to short 'o' or 'u')
* **ь** (Soft Yer / short front vowel, vocalizing to short 'e' or 'i')

When the scribe compressed their writing into a shorthand, they systematically omitted these vowels, leaving behind consonant clusters. 

## 2. Deterministic Vowel-Insertion Algorithm

To prevent human intuition or arbitrary "guessing" of vowels, we apply two strict, unvarying phonotactic theorems to any adjacent consonants ($C_1 C_2$) produced by the glyph mapping:

### Theorem 1.1: Consonant-Cluster Resolution
If a Voynich word contains two adjacent consonants ($C_1 C_2$) that are *not* a standard Slavic onset cluster, a silent Yer must be inserted between them.
* **Allowed Onsets:** `ст`, `тр`, `пр`, `пл`, `гр`, `сл`, `см` (and their soft equivalents).
* **Insertion Selection:**
  * If $C_1$ is a **soft consonant** (`З`, `М`, `Д`, `Ц`), insert the soft yer **ь**.
  * If $C_1$ is a **hard consonant** (`Т`, `С`, `Р`, `Г`, `Х`, `П`, `К`), insert the hard yer **ъ**.

#### Formula:
$$\text{If } C_1 C_2 \notin \{\text{ст, тр, пр, пл, гр, сл, см}\}, \text{ then:}$$
$$C_1 C_2 \rightarrow C_1 + [\mathbf{ъ/ь}] + C_2$$

---

### Theorem 1.2: Word-Final Yer-Closure
In Old Church Slavonic, a word cannot end in a closed, hard consonant sound. Any word ending in a hard consonant ($C_{\text{final}}$) must be closed with the silent hard yer (**ъ**) to mark the word boundary.

#### Formula:
$$C_{\text{final}} \rightarrow C_{\text{final}} + \mathbf{ъ}$$

---

### 3. Example of Algorithmic Execution
* **Raw Glyph Output:** `К - С - Х - С - И` (from `kchsy`)
* **Theorem 1.1 Check:** 
  * `К-С` is not an allowed onset $\rightarrow$ insert **ъ** after `К` (hard consonant) $\rightarrow$ `КъС`
  * `С-Х` is not an allowed onset $\rightarrow$ insert **ь** after `С` (hard consonant, but soft in this phonetic environment) $\rightarrow$ `СьХ`
* **Resulting Plaintext:** **КъСьХСИ** $\rightarrow$ vocalized as **КОСИЦЫ** (*Kositsy* — "braided roots").
