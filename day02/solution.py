#!/usr/bin/env python3
# coding: utf-8


import os
import re


def part1(lines):
    x, y = 0, 0

    for line in lines:
        m = re.match("(forward|down|up) (\d+)", line)
        command, units = m.groups()
        units = int(units)

        # If using Python 3.10+, can use switch statement
        if command == "forward":
            x += units
        elif command == "down":
            y += units
        elif command == "up":
            y -= units

    return x * y


def part2(lines):
    x, y, aim = 0, 0, 0

    for line in lines:
        m = re.match("(forward|down|up) (\d+)", line)
        command, units = m.groups()
        units = int(units)

        # If using Python 3.10+, can use switch statement
        if command == "forward":
            x += units
            y += aim * units
        elif command == "down":
            aim += units
        elif command == "up":
            aim -= units

    return x * y


def main():
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, "input.txt")
    with open(inputfile) as f:
        lines = f.read().splitlines()
        print(f"part1: {part1(lines)}")  # 1728414
        print(f"part2: {part2(lines)}")  # 1765720035


if __name__ == "__main__":
    main()
