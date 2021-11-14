"""
Given a roman numeral, convert it to an integer.
    ● 1 <= s.length <= 15
    ● s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    ● It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


# Reverse string (Runtime: 49 ms, Memory Usage: 14.3 MB)
def convert_roman(s: str) -> int:
    roman_numbers: dict[str, int] = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s: str = s[::-1]
    total: int = 0
    highest: int = 0
    for char in s:
        value: int = roman_numbers[char]
        if value >= highest:
            highest = value
            total += value
        else:
            total -= value
    return total


def main():
    s: str = "MMMCMXCIX"
    print(convert_roman(s))


if __name__ == '__main__':
    main()
