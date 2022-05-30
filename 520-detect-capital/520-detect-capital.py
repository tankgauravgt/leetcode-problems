class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(list(map(lambda x: x.isupper(), word))):
            return True
        elif all(list(map(lambda x: x.islower(), word))):
            return True
        elif len(word) > 0 and word[0].isupper() and all(list(map(lambda x: x.islower(), word[1::]))):
            return True
        else:
            return False