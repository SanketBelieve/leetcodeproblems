'''
s=input()
s_li=list(map(str(input())))
print(s_li)
'''
def longest_common_prefix(strs):
    """
    Finds the longest common prefix string among an array of strings.

    Args:
    - strs: A list of strings.

    Returns:
    - The longest common prefix string as a string. If there is no common prefix, an empty string is returned.
    """
    if not strs:
        return ""

    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix
print(longest_common_prefix(['flower','floght','flow']))