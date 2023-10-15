# def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
#     n=len(paragraph)
#     s=''
#     for i in range(len(n)):
        
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
a=paragraph.split()
banned = "hit"
s=0

for i in a:
    if banned in i:
        print(i)
        s+=1
print(s)    
      