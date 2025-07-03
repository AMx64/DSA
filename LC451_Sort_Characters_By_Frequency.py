from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        s_freq = Counter(s)
        s_sort = s_freq.most_common()
        ans = ""
        for i in range(len(s_sort)):
            ans += s_sort[i][0] * s_sort[i][1]

        return ans