#!/usr/bin/env python3
# coding: utf-8


import os


class Card:
    def __init__(self, num):
        self.num = num
        self.is_called = False

    def __repr__(self):
        if self.is_called:
            return f"{self.num}*"
        return f"{self.num}"


class Board:
    def __init__(self, grid):
        self.grid = grid
        self.is_bingo = False

    def __repr__(self):
        return f"Board: {self.grid}"

    def check_num(self, num):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].num == num:
                    self.grid[i][j].is_called = True
                    return

    def check_bingo(self):
        for row in self.grid:
            row_winners = list(filter(lambda c: c.is_called, row))
            if len(row_winners) == len(row):
                self.is_bingo = True
                return

        columns = list(zip(*self.grid))
        for column in columns:
            col_winners = list(filter(lambda c: c.is_called, column))
            if len(col_winners) == len(column):
                self.is_bingo = True
                return

    def get_unmarked_sum(self):
        sum_of_unmarked = 0
        for row in self.grid:
            for card in row:
                if not card.is_called:
                    sum_of_unmarked += card.num

        return sum_of_unmarked


def create_boards(lines):
    boards = []
    for i in range(2, len(lines), 6):
        board = Board([[Card(int(x)) for x in lines[i + y].split()] for y in range(5)])
        boards.append(board)
    return boards


def part1(lines):
    nums = list(map(int, lines[0].split(",")))
    boards = create_boards(lines)

    for num in nums:
        for board in boards:
            board.check_num(num)
            board.check_bingo()

            if board.is_bingo:
                return num * board.get_unmarked_sum()


def part2(lines):
    nums = list(map(int, lines[0].split(",")))
    boards = create_boards(lines)

    for num in nums:
        for board in boards:
            board.check_num(num)
            board.check_bingo()

            if len(list(filter(lambda b: not b.is_bingo, boards))) == 0:
                return num * board.get_unmarked_sum()


def main():
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, "input.txt")
    with open(inputfile) as f:
        data = f.read().splitlines()
        print(f"part1: {part1(data)}")  # 27027
        print(f"part2: {part2(data)}")  # 36975


if __name__ == "__main__":
    main()
