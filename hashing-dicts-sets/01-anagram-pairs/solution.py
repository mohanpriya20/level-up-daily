# Anagram Pairs in Two Lists — solution
from collections import defaultdict

def anagram_pairs(list1, list2):
    """
    Return the number of pairs (s1, s2) with s1 in list1, s2 in list2
    such that s1 and s2 are anagrams of each other.
    """
    pairs = []
    d1 = defaultdict(list)
    d2 = defaultdict(list)
    for word in list1:
        d1[tuple(sorted(word))].append(word)
    for word in list2:
        d2[tuple(sorted(word))].append(word)
    common_words=set(d1.keys()) & set(d2.keys())
    for word in common_words:
        for w1 in d1[word]:
            for w2 in d2[word]:
                pairs.append((w1, w2))
    return pairs


if __name__ == "__main__":
    list1 = input("Enter first list (space-separated words): ").split()
    list2 = input("Enter second list (space-separated words): ").split()
    result = anagram_pairs(list1, list2)
    print("Anagram pairs:", result)
