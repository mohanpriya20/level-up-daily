# Caesar Cipher — explanation

## Idea

Shift each letter by a fixed number of positions in the alphabet. Only letters change; everything else (spaces, punctuation, digits) stays the same. The alphabet wraps: after `z` comes `a`, and after `Z` comes `A`.

## ASCII ranges

- **Uppercase:** `A` = 65, `Z` = 90 (26 letters).
- **Lowercase:** `a` = 97, `z` = 122 (26 letters).

We work in two separate ranges and use modulo to wrap.

## How the code works

For each character:

1. **Non-letter** — If `char.isalpha()` is false, we append the character as-is (spaces, commas, digits, etc. stay unchanged).

2. **Uppercase letter** — We treat the letter as a position 0–25 in the alphabet: `ord(char) - 65`. Add the shift, wrap with `% 26` so we stay in 0–25, then convert back to ASCII: `+ 65`. So the formula is `chr((ord(char) - 65 + shift) % 26 + 65)`.

3. **Lowercase letter** — Same idea with base 97: position in alphabet is `ord(char) - 97`, then `(position + shift) % 26`, then back to ASCII with `+ 97`. So `chr((ord(char) - 97 + shift) % 26 + 97)`.

## Why modulo 26?

There are 26 letters. Adding the shift can take us past 25 (e.g. `x` + 3 = 25 + 3 = 28). `% 26` brings the value back into 0–25, so the alphabet wraps (e.g. 28 % 26 = 2, which is `c`).

## Summary

- Subtract the base (65 or 97) to get a 0–25 index.
- Add the shift and take `% 26` to wrap.
- Add the base back and use `chr()` to get the encrypted letter.

Non-alphabetic characters are left unchanged.
