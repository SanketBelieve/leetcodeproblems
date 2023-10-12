def isOneBitCharacter( bits: list[int]) -> bool:
        count=0
        for i in bits[::-1][1:]:
            if i == 1:
                count+=1
            else:
                break
        return count %2 == 0  