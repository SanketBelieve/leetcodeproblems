
#balloon
text = "nlaebolko"
s=[]
for i in text:
    s.append(i)
print(s)    

def maxNumberOfBalloons(text: str) -> int:
    word = {'a':0, 'b':0,'l':0, 'n':0, 'o':0}
    double_char = ['l','o']
    for c in text:
        if c in word:
            word[c] += 1
    for c in double_char:
        word[c] //= 2
    return min(word.values())


