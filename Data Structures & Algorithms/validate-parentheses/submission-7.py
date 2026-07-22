class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = dict()
        mappings['('] = ')'
        mappings['{'] = '}'
        mappings['['] = ']'
        for char in s:
            if char in mappings.keys():
                stack.append(char)
            else:
                if len(stack) <= 0:
                    if char in mappings.values():
                        return False
                    break
                most_recent = stack.pop()
                if mappings[most_recent] != char:
                    return False
        if len(stack) > 0:
            return False
        return True
            