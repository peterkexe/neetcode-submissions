class Solution:

    class HashableCounter(collections.Counter):
        def __hash__(self):
            return hash(tuple(sorted(self.items())))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_to_words = {}
        for word in strs:
            # counter = self.HashableCounter(word)
            counter = frozenset(collections.Counter(word).items())
            if counter in counter_to_words:
                counter_to_words[counter].append(word)
            else:
                counter_to_words[counter] = [word]
        return [words for counter, words in counter_to_words.items()]