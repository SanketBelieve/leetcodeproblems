def removeDuplicates( s: str) -> str:
        ans=[]
        for i in s:
            if (len(ans)> 0 and ans[-1]==i):
                ans.pop()
            else:
                ans.append(i)   
        return ("".join(ans))        

print(removeDuplicates("abbaca"))