s = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]

# m_s=s

# for i in range(len(s)):
#     for j in range(len(sources)):
#         if indices[j]==i and s[i] in sources:
#             s=s.replace(s[i],targets[j])
# print(s)
            
def findReplaceString(s, indices, sources, targets):
    # Convert the string to a list of characters for easier manipulation
    s = list(s)
    
    # For each replacement operation
    for i in sorted(range(len(indices)), key=lambda x: -indices[x]):
        # If the source string occurs at the given index
        if all(s[indices[i]+j] == sources[i][j] for j in range(len(sources[i]))):
            # Replace the source string with the target string
            s[indices[i]:indices[i]+len(sources[i])] = targets[i]
    
    # Convert the list of characters back to a string
    return ''.join(s)
s = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]
print(findReplaceString(s,indices,sources,targets))