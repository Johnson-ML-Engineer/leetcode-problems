"""You are given two string arrays, queries and dictionary. All words in each array
 comprise of lowercase English letters and have the same length.

In one edit you can take a word from queries, and change any letter in it to any
 other letter. Find all words from queries that, after a maximum of two edits,
   equal some word from dictionary.

Return a list of all words from queries, that match with some word from dictionary 
after a maximum of two edits. Return the words in the same order they appear in
 queries."""

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for word in queries:
            if word not in dictionary:
                for dword in dictionary:
                    count = 0
                    for i in range(len(word)):
                        if word[i] == dword[i]:
                            count +=1
                    if len(word)-count <=2 and word not in result:
                        result.append(word)
            else:
                result.append(word)
            
        return result


                
           
                
            

        