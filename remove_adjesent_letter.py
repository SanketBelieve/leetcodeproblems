# s = "abbaca"

# for i in range(len(s)):
#     if s[i]==s[i+1]:
#         s.remove(s[i])
#     print(s)  
    
s = "abbaca"
i = 1  # Start from the second character

while i < len(s) - 1:
    for i in range(len(s)):
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]  # Remove the adjacent duplicate characters
            i = max(1, i - 1)  # Move the index back by 1
        else:
            i += 1  # Move to the next character

    print(s)
        
        
    
