widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"


def numberOfLines(widths: list[int], s: str) -> list[int]:
    pix = 0
    line = 1
    i = 0
    a = 97
    while i<len(s):
        if pix<=100:
            pix+=widths[ord(s[i])-a]
            i+=1
            if pix>100:
                line+=1
                pix=0
                i-=1
    return [line, pix]
        
        
        