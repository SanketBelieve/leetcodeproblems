def findWords(self, words: list[str]) -> list[str]:
        keyboard = {
            1: set("qwertyuiop"),
            2: set("asdfghjkl"),
            3: set("zxcvbnm")
        }
        
        # Step 2
        result = []
        
        # Step 3
        for word in words:
            word_lower = word.lower() # Step 3a
            row = None # Step 3b
            for key, value in keyboard.items():
                if word_lower[0] in value: # Check if the first character belongs to the current row
                    row = key
                    break
            if row is not None and all(char in keyboard[row] for char in word_lower): # Step 3d
                result.append(word)
        
        # Step 4
        return result
    
