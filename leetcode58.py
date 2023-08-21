'''
input = input("Enter a string:")
word = input.split()

last_word = word[-1]
print(len(last_word))
'''

def lengthOfLastWord( s: str) -> int:
        i , length = len(s)-1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length 
    
s=lengthOfLastWord("be the change you want to be") 
print(s)




   