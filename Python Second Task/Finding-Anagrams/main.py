# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False 


word = input('Enter first string:').lower().strip()
anagram = input('Enter second string:').lower().strip()
if(sorted(word)==sorted(anagram)):
       print("True")
else:
       print("False")