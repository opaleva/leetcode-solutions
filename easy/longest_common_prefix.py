"""
Write a function to find the longest common prefix string amongst an array of strings.
    ● 1 <= strings.length <= 200
    ● 0 <= strings[i].length <= 200
    ● strings[i] consists of only lower-case English letters.
"""


# Horizontal scanning (Runtime: 69 ms, Memory Usage: 14.4 MB)
def scan_horizontally(strings: list[str]) -> str:
    if len(strings) == 0:
        return "Strings not found"
    prefix: str = strings[0]
    for i in range(len(strings)):
        while strings[i].find(prefix) != 0:
            prefix = prefix[0:len(prefix) - 1]
            if prefix == "":
                return "No common prefix strings found"
    return prefix


# Vertical scanning (Runtime: 36 ms, Memory Usage: 14.3 MB)
def scan_vertically(strings: list[str]) -> str:
    if not strings or len(strings) == 0:
        return "Strings not found"
    for i in range(len(strings[0])):
        c: str = strings[0][i]
        for j in range(1, len(strings)):
            if i == len(strings[j]) or strings[j][i] != c:
                return strings[0][0:i]
    # return strings[0]


# Divide and conquer (Runtime: 52 ms, Memory Usage: 14.3 MB)
def get_longest(strings: list[str]) -> str:
    if not strings or len(strings) == 0:
        return "Strings not found"
    return divide(strings, 0, len(strings) - 1)


def divide(strings: list[str], left: int, right: int) -> str:
    if left == right:
        return strings[left]
    if right > left:
        middle: int = left + (right - left) // 2
        str1: str = divide(strings, left, middle)
        str2: str = divide(strings, middle + 1, right)
        return conquer(str1, str2)


def conquer(left_lcp, right_lcp):
    result: str = ""
    i, j = 0, 0
    while i <= len(left_lcp) - 1 and j <= len(right_lcp) - 1:
        if left_lcp[i] != right_lcp[j]:
            break
        result += left_lcp[i]
        i, j = i + 1, j + 1
    return result


def main():
    strings: list[str] = ["flower", "flow", "flight"]
    print(get_longest(strings))


if __name__ == '__main__':
    main()
