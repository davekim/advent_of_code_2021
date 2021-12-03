#!/usr/bin/env python3
# coding: utf-8


import os
import re

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    x, y = 0, 0

    for line in data:
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


def part2(data):
    x, y, aim = 0, 0, 0

    for line in data:
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
    day = os.path.basename(__file__).split('.')[0]
    print(day)
    with open(inputfile) as f:
        data = f.read().splitlines()
        print(f"part1: {part1(data)}") # 1728414
        print(f"part2: {part2(data)}") # 1765720035


if __name__ == "__main__":
    main()
