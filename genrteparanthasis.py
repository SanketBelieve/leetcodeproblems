def generateParenthesis( n: int) -> list[str]:
    res = []
    def dfs(path, left, right):             # takes the number of left and right brackets
        if left > n  or right > n: return   # if number of left or right brackets exceed n, return
        if left == right == n:  
            res.append(path)    # append path when n pairs of brackets are added
            return
            
        if left > right:    
            dfs(path + '(', left + 1, right)
            dfs(path + ')', left, right + 1)
            
            # when number of left brackets > right brackets, we can add left or right brackets
            
        else:
            dfs(path + '(', left + 1, right)    
            
            # when number of right brackets > left brackets, we can only add left brackets
    
    dfs('', 0, 0)   # start with left = right = 0
    return res

print(generateParenthesis(3))