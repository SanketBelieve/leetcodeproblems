#heystake=input("enter a word:")
#needle=input("enter a word:")
def strStr( haystack: str, needle: str) -> int:
    if haystack == "":
        return 0
    
    for i in range(len(haystack)+1 - len(needle)):
        for j in range(len(needle)):
            
            if haystack[i + j] != needle[j]:
                break
            if haystack[i+j]==needle[j]:
                return i   
    return -1    

p = strStr("sadbutsad","but")
print(p)