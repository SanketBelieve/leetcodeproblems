def titleToNumber( columnTitle: str) -> int:
        columnNumber = 0
        for char in columnTitle:
            columnNumber = columnNumber * 26 + (ord(char) - ord('A') + 1)
        return columnNumber    

print(titleToNumber('AXB'))