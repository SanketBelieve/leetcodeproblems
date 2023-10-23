# words = ["bella","label","roller"]
# s=[]
# for i in words:
#     for j in i:
#         if i[j]==i[j+1]:
#             s.append(i)
# print(s)            

def commonChars(words: list[str]) -> list[str]:
        res = Counter(words[0])
        for i in words:
            res &= Counter(i)
        return list(res.elements())