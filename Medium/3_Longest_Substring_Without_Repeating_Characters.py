# 3. Longest Substring Without Repeating Characters


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        ans = 0
        temp = ""

        # i = 0
        j = 0

        while j < size:
            if s[j] not in temp:
                temp += s[j]
                j += 1
                ans = max(ans, len(temp))
            else:
                temp = temp[1:]
                # i += 1

        return ans