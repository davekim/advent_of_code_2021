# coding: utf-8
#!/usr/bin/env python3


import os


def parse_vent_line(line):
    start, end = line.split(" -> ")
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")
    return map(int, [x1, y1, x2, y2])


def calculate_points(line, diagonals=False):
    x1, y1, x2, y2 = parse_vent_line(line)

    min_x = min(x1, x2)
    max_x = max(x1, x2)

    min_y = min(y1, y2)
    max_y = max(y1, y2)

    x_range = range(min_x, max_x + 1)
    y_range = range(min_y, max_y + 1)

    points = []
    if min_y == max_y:
        for x in x_range:
            points.append((x, min_y))
    elif min_x == max_x:
        for y in y_range:
            points.append((min_x, y))
    elif diagonals:
        slope = (y2 - y1) // (x2 - x1)
        if slope < 0:
            y_range = range(max_y, min_y - 1, slope)
        else:
            y_range = range(min_y, max_y + 1, slope)

        for x, y in zip(x_range, y_range):
            points.append((x, y))
    return points


def create_grid(lines, diagonals=False):
    width, height = 0, 0
    for line in lines:
        x1, y1, x2, y2 = parse_vent_line(line)
        width = max(width, x1, x2)
        height = max(height, y1, y2)

    grid = Grid(width, height)

    for line in lines:
        grid.add_line_segment(line, diagonals)
    return grid


class Grid:
    def __init__(self, width, height):
        self.points = [[0 for x in range(width + 1)] for y in range(height + 1)]

    def add_line_segment(self, line, diagonals=False):
        points = calculate_points(line, diagonals)
        for point in points:
            x, y = point
            self.points[y][x] += 1

    def count_overlaps(self):
        count = 0
        for row in self.points:
            for point in row:
                if point >= 2:
                    count += 1
        return count

    def __repr__(self):
        return f"Grid: {self.grid}"


def get_input_lines(filename):
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, filename)

    with open(inputfile) as f:
        return f.read().splitlines()


def part1(lines):
    grid = create_grid(lines)
    return grid.count_overlaps()


def part2(lines):
    grid = create_grid(lines, True)
    return grid.count_overlaps()


def main():
    lines = get_input_lines("input.txt")
    print(f"part1: {part1(lines)}")  # 4993
    print(f"part2: {part2(lines)}")  # 21101


if __name__ == "__main__":
    main()
