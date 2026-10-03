# Ligature Decomposition Matrix

This document details the second mathematical layer of the **Per-Ankh Key**: the geometric rules for expanding connected or fused glyphs (ligatures) in the Voynich script.

## 1. Defining the Gallows Glyphs
The "gallows" characters (the base glyphs with vertical ascending stems, transcribed in EVA as `t`, `p`, `k`, `f`) represent the core consonants of the cipher. In the scribe's cursive hand, these characters are frequently fused with secondary loops or bars.

## 2. Geometric Decomposition Rules

To ensure reproducible expansion of fused characters, we apply three strict visual matrices:

### Rule 2.1: The Left-Loop Extension
* **Visual Marker:** A rounded loop attached to the left vertical stem of a gallows glyph.
* **Decomposition:** The left loop represents a prefixed soft sign (**ь**) or a palatalizing glide (**й** / **i**) preceding the consonant.

#### Formula:
$$\text{Loop} + \text{Gallows } (C) \rightarrow \mathbf{ь} + C$$

---

### Rule 2.2: The Double Gallows Bridge
* **Visual Marker:** Two gallows glyphs joined together by a single, continuous horizontal bar at the top (transcribed in EVA as `cth` or `cfh`).
* **Decomposition:** The bridging horizontal bar represents the consonant **С** (*Slovo*) prefixed to the second consonant.

#### Formula:
$$\text{Gallows}_1 + \text{Bridge} + \text{Gallows}_2 \rightarrow \mathbf{С} + C_2$$

---

### Rule 2.3: The Right-Loop Tail
* **Visual Marker:** A loop or hook extending from the right stem of a consonant descending below the line.
* **Decomposition:** Represents a palatalized vowel or soft sign suffix (**ь** or **я**) appended to the end of the consonant.

#### Formula:
$$\text{Gallows } (C) + \text{Right-Loop} \rightarrow C + \mathbf{ь}$$
