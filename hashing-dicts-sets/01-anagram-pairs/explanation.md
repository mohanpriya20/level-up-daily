# Anagram Pairs in Two Lists — explanation

## Idea

Two words are anagrams if they have the same letters in a different order (e.g. "cat" and "act"). We want all pairs (word from list1, word from list2) that are anagrams. We group words by a canonical form so anagrams fall into the same bucket, then pair everything across the two lists for each bucket.

## Canonical form: sorted tuple

Anagrams have the same multiset of characters. A simple canonical form is to sort the word and use that as a key: `tuple(sorted(word))`. So "cat", "act", "tac" all become `('a', 'c', 't')`. We use a tuple (not a list) because dict keys must be hashable.

## Two dictionaries

- **d1** — For each word in list1, we use `tuple(sorted(word))` as the key and append the word to the list at that key. So d1 maps each “anagram signature” to the list of words from list1 with that signature.
- **d2** — Same for list2.

## Finding pairs

We only get pairs when both lists have at least one word with the same signature. So we take the set of keys that appear in both: `common_keys = set(d1.keys()) & set(d2.keys())`. For each such key, every word in `d1[key]` is an anagram of every word in `d2[key]`, so we do two nested loops and append `(w1, w2)` for each combination. That gives the full list of anagram pairs.

## Why this works

Grouping by sorted tuple puts all anagrams in the same bucket. Intersecting keys restricts to signatures present in both lists. Enumerating all (w1, w2) for each common key produces exactly the anagram pairs, including duplicates if the same word or signature appears more than once in either list.
