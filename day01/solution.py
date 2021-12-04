#!/usr/bin/env python3
# coding: utf-8


import os


def part1(data):
    previous = float("inf")
    count = 0
    for line in data:
        num = int(line)
        if num > previous:
            count += 1
        previous = num
    return count


def part2(data):
    nums = list(map(int, data))
    window_size = 3
    windows = len(nums) - window_size + 1
    window_sums = [sum(nums[i : i + window_size]) for i in range(windows)]
    return part1(window_sums)


def main():
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, "input.txt")
    with open(inputfile) as f:
        data = f.read().splitlines()
        print(f"part1: {part1(data)}")  # 1681
        print(f"part2: {part2(data)}")  # 1704


if __name__ == "__main__":
    main()
