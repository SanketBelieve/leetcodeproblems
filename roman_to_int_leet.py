def int_to_roman(num):
    roman_numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    decimal_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numeral = ""
    i = 0
    while num > 0:
        if num >= decimal_values[i]:
            roman_numeral += roman_numerals[i]
            num -= decimal_values[i]
        else:
            i += 1
    return roman_numeral
print(int_to_roman(1012))