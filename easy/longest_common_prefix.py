"""
Write a function to find the longest common prefix string amongst an array of strings.
    ● 1 <= strs.length <= 200
    ● 0 <= strs[i].length <= 200
    ● strs[i] consists of only lower-case English letters.
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


# Vertical scanning
def scan_vertically(strings: list[str]) -> str:
    pass


def main():
    strings = []
    print(scan_horizontally(strings))


if __name__ == '__main__':
    main()