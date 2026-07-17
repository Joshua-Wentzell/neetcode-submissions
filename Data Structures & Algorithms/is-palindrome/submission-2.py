class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
        length = len(cleaned)
        if length % 2 != 0:
            length -= 1
        length = length // 2
        for i in range(length):
            if cleaned[i].lower() != cleaned[-(i + 1)].lower():
                return False
        return True