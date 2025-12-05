def get_adjacent_indices(
    row: int,
    col: int,
    num_rows: int,
    num_cols: int,
) -> list[tuple[int, int]]:
    """
    For a given array size and `row, col` coordinates, return all indices of adjacent spots.
    """
    if (row < 0) or (row >= num_rows):
        raise ValueError(f"illegal row: {row} (must be between 0 and {num_rows})")
    if (col < 0) or (col >= num_cols):
        raise ValueError(f"illegal column: {col} (must be between 0 and {num_cols})")
    
    # four corners: 3 adjacent coords each
    # top left
    if (row == 0) and (col == 0):
        return [(0, 1), (1, 0), (1, 1)]
    # top right
    if (row == 0) and (col == num_cols - 1):
        return [(0, num_cols - 2), (1, num_cols - 2), (1, num_cols - 1)]
    # bottom left
    if (row == num_rows - 1) and (col == 0):
        return [(num_rows - 2, 0), (num_rows - 2, 1), (num_rows - 1, 1)]
    # bottom right
    if (row == num_rows - 1) and (col == num_cols - 1):
        return [(num_rows - 2, num_cols - 2), (num_rows - 2, num_cols - 1), (num_rows - 1, num_cols - 2)]
    
    # four sides: 5 adjacent coords each
    # top
    if row == 0:
        return [(0, col - 1), (0, col + 1), (1, col - 1), (1, col), (1, col + 1)]
    # left
    if col == 0:
        return [(row - 1, 0), (row - 1, 1), (row, 1), (row + 1, 0), (row + 1, 1)]
    # right
    if col == num_cols - 1:
        return [(row - 1, num_cols - 2), (row - 1, num_cols - 1), (row, num_cols - 2), (row + 1, num_cols - 2), (row + 1, num_cols - 1)]
    # bottom
    if row == num_rows - 1:
        return [(num_rows - 2, col - 1), (num_rows - 2, col), (num_rows - 2, col + 1), (num_rows - 1, col - 1), (num_rows - 1, col + 1)]
    
    # middle section: 8 adjacent coords each
    return [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1)
    ]


def num_true(
    array: list[list[bool]],
    adjacents: list[tuple[int, int]]
) -> int:
    """
    Determine how many `True` values exist in the adjacent coordinates for the given array.
    """
    count_true = 0
    for row, col in adjacents:
        if array[row][col]:
            count_true += 1
    
    return count_true