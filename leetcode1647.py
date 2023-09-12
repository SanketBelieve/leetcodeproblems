import collections
def minDeletions(s: str) -> int:
        delegation=0
        char_count=collections.Counter(s)
        freq_set=set()
        for char , count in char_count.items():
            while count > 0 and count in freq_set:
                count -= 1
                delegation +=1
            freq_set.add(count)
        return delegation        