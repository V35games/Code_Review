"""
Given a string s, find the length of the longest substring without repeating characters.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        max_len = 0
        curr_len = 0
        i = 0
        start_index = 0
        n = len(s)
        while i < n:
            #print(s[i])
            #print(seen.keys())
            if s[i] not in seen:
                seen[s[i]] = True 
                curr_len += 1
                #print("curr len: ", curr_len)
                if curr_len > max_len:
                    max_len = curr_len
                    #print("max len: ", max_len)
                i += 1
            else:
                #print("================resetting")
                seen.clear()
                curr_len = 0
                start_index += 1
                i = start_index
                # if i < n:
                #     seen[s[i]] = True
        return max_len

sol = Solution()
print(sol.lengthOfLongestSubstring("aab"))
#print(sol.lengthOfLongestSubstring("dvdf"))
