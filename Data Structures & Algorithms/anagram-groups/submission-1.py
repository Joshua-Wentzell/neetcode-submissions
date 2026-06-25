class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_result = []

        new_strs = []
        for i in range(len(strs)):
            new_strs.append("".join(sorted(strs[i])))

        visited = []
        for i in range(len(new_strs)):
            this_group = []
            if i not in visited:
                visited.append(i)
                this_group.append(strs[i])
                for j in range(len(new_strs)):
                    if j not in visited:
                        if new_strs[i] == new_strs[j]:
                            this_group.append(strs[j])
                            visited.append(j)
                final_result.append(this_group)

        return final_result