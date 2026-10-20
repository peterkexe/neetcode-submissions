class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += word + '¥'
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = s.split('¥')
        # decoded[-1].rstrip('¥')
        decoded = decoded[:-1]
        return decoded