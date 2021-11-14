"""
Given a roman numeral, convert it to an integer.
    ● 1 <= s.length <= 15
    ● s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    ● It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


def convert_roman(s):
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = s[::-1]
    total = 0
    highest = 0
    for char in s:
        value = roman_numbers[char]
        if value >= highest:
            highest = value
            total += value
        else:
            total -= value
    return total


def main():
    s = "MMMCMXCIX"
    print(convert_roman(s))


if __name__ == '__main__':
    main()
