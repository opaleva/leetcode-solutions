"""
Given an array of integers nums and an integer target, return indices of the 2 numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
from random import randint


# Brute force (Runtime: 6229 ms, Memory Usage: 14.7 MB)
def get_indices(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]


# Two-pass hash table (Runtime: 106 ms, Memory Usage: 15.5 MB)
def pass_twice(nums: list[int], target: int) -> list[int]:
    table: dict[int, int] = {}
    for i in range(len(nums)):
        table[nums[i]] = i
    for i in range(len(nums)):
        second_number: int = target - nums[i]
        if second_number in table and table[second_number] != i:
            return [i, table[second_number]]


# One-pass hash table (Runtime: 114 ms, Memory Usage: 15.2 MB)
def pass_once(nums: list[int], target: int) -> list[int]:
    table: dict[int, int] = {}
    for i in range(len(nums)):
        second_number: int = target - nums[i]
        if second_number in table:
            return [i, table[second_number]]
        table[nums[i]] = i


def main():
    nums: list[int] = [randint(0, 20) for _ in range(20)]
    target: int = randint(0, 40)
    print(f"{nums}\n{target}")
    if pass_once(nums, target):
        print(f"{pass_once(nums, target)}")
    else:
        print("No matching numbers found")


if __name__ == '__main__':
    main()
