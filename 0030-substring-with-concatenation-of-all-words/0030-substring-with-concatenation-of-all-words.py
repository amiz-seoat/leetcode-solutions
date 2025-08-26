from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        substring_len = word_len * word_count
        word_map = Counter(words)

        result = []

        # We need to check starting from every offset in [0, word_len)
        for i in range(word_len):
            left = i
            right = i
            curr_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_map:
                    curr_count[word] += 1

                    # If more than needed, shrink from left
                    while curr_count[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len

                    # If window size matches substring_len, record result
                    if right - left == substring_len:
                        result.append(left)
                else:
                    # Reset if invalid word
                    curr_count.clear()
                    left = right

        return result
