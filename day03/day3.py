# coding: utf-8
#!/usr/bin/env python3


import os
from collections import Counter


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')



def part1(lines):
    gamma, epsilon = "", ""

    for vertical_bits in zip(*map(list, lines)):
        c = Counter(vertical_bits)
        if c['1'] > c['0']:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def part2(lines):
    length = len(lines[0])
    oxygen_candidates = lines
    co2_candidates = lines

    for i in range(length):
        vertical_bits = list(zip(*map(list, oxygen_candidates)))
        c = Counter(vertical_bits[i])

        if c['1'] >= c['0']:
            oxygen_candidates = [x for x in oxygen_candidates if x[i] == '1'][:c['1']]

        elif c['1'] < c['0']:
            oxygen_candidates = [x for x in oxygen_candidates if x[i] == '0'][:c['0']]

        if len(oxygen_candidates) == 1:
            break

    for i in range(length):
        vertical_bits = list(zip(*map(list, co2_candidates)))
        c = Counter(vertical_bits[i])

        if c['0'] <= c['1']:
            co2_candidates = [x for x in co2_candidates if x[i] == '0'][:c['0']]

        elif c['0'] > c['1']:
            co2_candidates = [x for x in co2_candidates if x[i] == '1'][:c['1']]

        if len(co2_candidates) == 1:
            break

    return int(oxygen_candidates[0], 2) * int(co2_candidates[0], 2)


def main():
    day = os.path.basename(__file__).split('.')[0]
    print(day)
    with open(inputfile) as f:
        data = f.read().splitlines()
        print(f"part1: {part1(data)}") # 2954600
        print(f"part2: {part2(data)}") # 1662846


if __name__ == "__main__":
    main()
