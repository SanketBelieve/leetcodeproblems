d = ["a","b","c"]
s = "aadsfasf absbs bbab cadsfafs"
#Output: "a a b c"
p=s.split()
#p.remove(p[0])
ns=''
print(p)
for i in range(len(d)):
    for j in range(len(p)):
        if d[i]==p[j][0:len(d[i])]:
            ns+=d[i]
            ns+=' '        
          
print(ns) 
# k=[]
# for i in range(len(d)-1,-1,-1):          
#     for j in range(len(p)-1,-1,-1):
#         #print(p[i])   
#         if d[i] in p[j][0:len(d[i])]:
#             k.append(d[i])
#         else:
#             k.append(p[j])    
# print(k)           
# # print(p)
# for i in range(len(p)):
    #print(p[i])
    # for i in d:
    #     if i in p[i]:
    #         print(i)
dictionary = ["a","b","c"]
sentence= "aadsfasf absbs bbab cadsfafs"
sentence = sentence.split()
new = []

for sen in range(len(sentence)):
    successor=sentence[sen]
    for word in dictionary:
        if successor.startswith(word):
            if len(word) < len(successor):
                successor = word
        # print(sentence[sen])
            
    sentence[sen] = successor
print(' '.join(sentence))
