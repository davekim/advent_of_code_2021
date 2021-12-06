import os
from solution import get_input_lines, calculate_points, create_grid


def test_calculate_points():
    assert sorted([(1, 1), (1, 2), (1, 3)]) == sorted(
        calculate_points("1,1 -> 1,3", False)
    )
    assert sorted([(9, 7), (8, 7), (7, 7)]) == sorted(
        calculate_points("9,7 -> 7,7", False)
    )
    assert sorted([]) == sorted(calculate_points("8,0 -> 0,8", False))
    assert sorted([(1, 1), (2, 2), (3, 3)]) == sorted(
        calculate_points("1,1 -> 3,3", True)
    )
    assert sorted([(9, 7), (8, 8), (7, 9)]) == sorted(
        calculate_points("9,7 -> 7,9", True)
    )
    assert sorted([(5, 5), (7, 3), (6, 4), (8, 2)]) == sorted(
        calculate_points("5,5 -> 8,2", True)
    )


def get_str_representation(grid):
    reps = []
    for row in grid:
        row_str = ""
        for num in row:
            if num == 0:
                row_str += "."
            else:
                row_str += str(num)
        reps.append(row_str)

    return reps


def test_grid_state_for_part_1_with_test_data():
    lines = get_input_lines("test.txt")
    grid = create_grid(lines, False)
    expected = [
        ".......1..",
        "..1....1..",
        "..1....1..",
        ".......1..",
        ".112111211",
        "..........",
        "..........",
        "..........",
        "..........",
        "222111....",
    ]
    assert expected == get_str_representation(grid.points)


def test_grid_state_for_part_2_with_test_data():
    lines = get_input_lines("test.txt")
    grid = create_grid(lines, True)
    expected = [
        "1.1....11.",
        ".111...2..",
        "..2.1.111.",
        "...1.2.2..",
        ".112313211",
        "...1.2....",
        "..1...1...",
        ".1.....1..",
        "1.......1.",
        "222111....",
    ]
    assert expected == get_str_representation(grid.points)


if __name__ == "__main__":
    test_calculate_points()
    test_grid_state_for_part_1_with_test_data()
    test_grid_state_for_part_2_with_test_data()
    print("All tests passed! ✨")
