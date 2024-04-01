def letterCasePermutation(s):
    def backtrack(s, index, current, result):
        # If we've processed all characters, add the current string to the result
        if index == len(s):
            result.append(current)
            return

        # If the current character is a letter, explore both lowercase and uppercase possibilities
        if s[index].isalpha():
            backtrack(s, index + 1, current + s[index].lower(), result)
            backtrack(s, index + 1, current + s[index].upper(), result)
        else:
            # If the current character is not a letter, keep it unchanged
            backtrack(s, index + 1, current + s[index], result)

    result = []
    backtrack(s, 0, "", result)
    return result

# Example usage:
s = "a1b2"
print(letterCasePermutation(s))
