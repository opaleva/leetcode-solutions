"""
Given an array of integers nums and an integer target, return indices of the 2 numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
from random import randint


def get_indices(nums: list[int], target: int) -> list[int]:
    table = {}
    for i in range(len(nums)):
        second_number = target - nums[i]
        if second_number in table:
            return [i, table[second_number]]
        table[nums[i]] = i


def main():
    nums = [randint(0, 20) for _ in range(20)]
    target = randint(0, 40)
    print(f"{nums}\n{target}")
    if get_indices(nums, target):
        print(f"{get_indices(nums, target)}")
    else:
        print("No matching numbers found")


if __name__ == '__main__':
    main()
