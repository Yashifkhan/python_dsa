print("learn string ")
# count the frequince of characters
# s="yashiff"
# def count_freq(s):
#     freq={}
#     for ch in s:
#         if ch in freq:
#             freq[ch] += 1
#         else :
#             freq[ch]=1
#     return freq
    
# print(count_freq(s))

# Problem: Check if a string is a palindrome
# s='mamghfg'

# def is_palindrom(s):
#     first=0
#     last=len(s)-1
#     while first<last:
#        if s[first] != s[last]:
#            return "not anagram"
#        first+=1
#        last-=1
#     return "anageram"

# print(is_palindrom(s))

# string are anagram or not 
# s1 = "aab"
# s2 = "aba"

# def is_anagram(s1,s2):
#     if len(s1) == len(s2):
#         print("count is same move next step")
#     else:
#         return 
    
#     freq={}
#     for ch in s1:
#         if ch in freq:
#             freq[ch]+=1
#         else:
#             freq[ch]=1

#     for ch in s2:
#         if ch  not in freq or freq[ch] ==0:
#             return False
#         freq[ch]-=1
#     return "anagram"

# print(is_anagram(s1,s2))


# SUBSTRINGS
# A substring is a continuous part of a string
# Generate All Substrings

# s="yashif"
# def sub_str(s):
#     for i in range(len(s)):
#         for j in range(i+1,len(s)+1):
#             print (s[i:j])
# print(sub_str(s))