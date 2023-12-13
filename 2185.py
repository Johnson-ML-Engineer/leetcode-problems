"""You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s."""

class Solution:
    def prefixCount(self, words, pref):
        count = 0
        for word in words:
            if pref in word[:len(pref)]:
                count += 1
        return count