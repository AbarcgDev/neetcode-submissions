class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            s_word = "".join(sorted(word))
            anagrams[s_word].append(word)
        
        
        return [value for key, value in anagrams.items()]