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
        return ""
    for i in range(len(strings[0])):
        c: str = strings[0][i]
        for j in range(1, len(strings)):
            if i == len(strings[j]) or strings[j][i] != c:
                return strings[0][0:i]
    return strings[0]


def main():
    strings = ["flower", "flow", "flight"]
    print(scan_vertically(strings))


if __name__ == '__main__':
    main()
