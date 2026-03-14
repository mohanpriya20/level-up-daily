# Keyword index — explanation

## Idea

We have a list of documents (strings). We want a lookup structure: for each word that appears in any document, we want to know in which documents it appears and how many times in each. So the output is a dict: word → {doc_index: count}. That’s a simple inverted index over words.

## Structure

We use a nested structure while building: `d[word][doc_index]` will hold the count of that word in that document. So we need a dict of dicts, and the inner dict should default to 0 for missing (doc_index, count). That’s why we use `defaultdict(lambda: defaultdict(int))`: the outer key is the word, the inner key is the document index, the value is the count.

## How we fill it

We loop over documents with `enumerate(docs)` so we have `index` (0, 1, 2, …) for each document. For each document we split on whitespace with `doc.split()` to get words. For each word we do `d[word][index] += 1`: we’re counting how many times that word appears in that document. The defaultdicts take care of creating missing keys and starting at 0.

## Return value

The problem expects a plain dict whose values are plain dicts, not defaultdicts. So we convert before returning: `{word: dict(counts) for word, counts in d.items()}`. That turns the outer defaultdict and each inner defaultdict(int) into normal dicts, so the output looks like `{'Hello': {0: 1}, 'world': {0: 1, 1: 1}, ...}` and is easy to read and use.

## Edge cases

- Empty `docs`: we never enter the loop, so we return an empty dict (from the comprehension over `d.items()`).
- Empty string in `docs`: `"".split()` is `[]`, so we don’t add any words for that document.
- Repeated word in one doc: we hit `d[word][index] += 1` multiple times, so the count for that (word, doc) is correct.
