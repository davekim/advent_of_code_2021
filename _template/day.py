#!/usr/bin/env python3
# coding: utf-8


import os


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    pass


def part2(data):
    pass


def main():
    day = os.path.basename(__file__).split('.')[0]
    print(day)
    with open(inputfile) as f:
        data = f.read().splitlines()
        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")


if __name__ == "__main__":
    main()
