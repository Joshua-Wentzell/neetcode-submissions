class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "\ue001"
        separator = "\ue000"
        return separator.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "\ue001":
            return []
        separator = "\ue000"
        return s.split(separator)