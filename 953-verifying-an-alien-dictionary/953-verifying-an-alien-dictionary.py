class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        a2e = dict(zip(order, "abcdefghijklmnopqrstuvwxyz"))
        for ix, word in enumerate(words):
            words[ix] = list(map(lambda c: a2e[c], word))
        sorted_words = sorted(words)
        
        return sorted_words == words