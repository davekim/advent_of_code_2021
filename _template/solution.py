#!/usr/bin/env python3
# coding: utf-8


import os


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, "input.txt")
    with open(inputfile) as f:
        lines = f.read().splitlines()
        print(f"part1: {part1(lines)}")
        print(f"part2: {part2(lines)}")


if __name__ == "__main__":
    main()
