class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_result = []
        counts = dict(dict())
        for i in range(len(strs)):
            char_dict = dict()
            for char in strs[i]:
                if char not in char_dict:
                    char_dict[char] = 1
                else:
                    char_dict[char] += 1
            counts[i] = char_dict

        visited = []
        for i in range(len(strs)):
            if i not in visited:
                visited.append(i)
                this_group = [strs[i]]
                for j in range(len(strs)):
                    if j not in visited:
                        if counts[i] == counts[j]:
                            this_group.append(strs[j])
                            visited.append(j)
                final_result.append(this_group)

        return final_result