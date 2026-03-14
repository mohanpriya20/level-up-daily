# Keyword index — solution
from collections import defaultdict
def keyword_index(docs):
    """
    docs: list of strings (documents).
    Return: dict mapping each unique word to a dict {doc_index: count in that doc}.
    """
    d = defaultdict(lambda: defaultdict(int))
    for index, doc in enumerate(docs):
        for word in doc.split():
            d[word][index]+=1
    return {word: dict(counts) for word, counts in d.items()}


if __name__ == "__main__":
    docs = ["Hello world", "world of python", "python is a snake"]
    print(keyword_index(docs))
    # Expected: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}
