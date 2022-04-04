""" Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    Constraints:
        - 1 <= strs.length <= 104
        - 0 <= strs[i].length <= 100
        - strs[i] consists of lowercase English letters.

    Example 1:
        - Input: strs = ["eat","tea","tan","ate","nat","bat"]
        - Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    Example 2:
        - Input: strs = [""]
        - Output: [[""]]
    Example 3:
        - Input: strs = ["a"]
        - Output: [["a"]] """

def group_anagrams(n):
    dl={}
    for i in n:
        key = "".join(sorted(i))
        if key not in dl: dl[key] =[i]
        else: dl[key].append(i)

    return sorted(list(dl.values()))

if __name__=='__main__':
    # n= int(input("number of length: "))
    # lstr = list(input().split())

    lstr = ["eat","tea","tan","ate","nat","bat"]
    print("Output: ",group_anagrams(lstr))
    lstr = [""]
    print("Output: ",group_anagrams(lstr))
    lstr = ["a"]
    print("Output: ",group_anagrams(lstr))