#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


#Time:O(n), O(1)
class Solution:
    def anagram(self, strs):
        dic = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]

        return dic.values()
