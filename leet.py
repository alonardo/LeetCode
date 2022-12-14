# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
            
        return True

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return 
        
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.        
class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
            
        return res.values()
                
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.        

class Solution(object):
    def isPalindrome(self, s):
        new_str = ""
        
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]

# Two pointer
class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s) -1
        
        while l < r:
            while l < r and not self.alpha_num(s[l]):
                l += 1
            while r > l and not self.alpha_num(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
        
    def alpha_num(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
         ord('a') <= ord(c) <= ord('z') or
         ord('0') <= ord(c) <= ord('9'))
    