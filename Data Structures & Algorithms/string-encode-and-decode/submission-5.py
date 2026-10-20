class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + '#' + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            num = ""
            while s[i] != '#':
                num += s[i]
                i += 1
            i += 1
            num = int(num)
            word = ""
            for j in range(num):
                word += s[i]
                i += 1
            decoded.append(word)
        return decoded

    # def encode(self, strs: List[str]) -> str:
    #     encoded = ""
    #     for word in strs:
    #         encoded += word + '¥'
    #     return encoded

    # def decode(self, s: str) -> List[str]:
    #     decoded = s.split('¥')
    #     decoded = decoded[:-1]
    #     return decoded