#!/usr/bin/env python3
# coding: utf-8


import os


def part1(data):
    pass


def part2(data):
    pass


def main():
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, "input.txt")
    with open(inputfile) as f:
        data = f.read().splitlines()
        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")


if __name__ == "__main__":
    main()
