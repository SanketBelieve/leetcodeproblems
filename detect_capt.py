word="USa"
if word.isupper():
    print(True)
else:
    print(False)    

def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        else:
            return False    