def readBinaryWatch(self, turnedOn: int) -> List[str]:
        out=[]
        for h in range(12):
            for m in range(60):
                temp=bin(h)+bin(m)
                if temp.count("1")==turnedOn:
                    time='%d:%02d'% (h,m)
                    out.append(time)
        return out            
                