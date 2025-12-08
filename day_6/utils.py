def product(
    l: list[int],
) -> int:
    """
    Get the product of all integers in this list.
    """
    result = 1
    for elem in l:
        result *= elem

    return result


def array_of_zeros(
    rows: int,
    cols: int,
) -> list[list[int]]:
    """
    Create a 2-dimensional list of ints, all set to 0.
    """
    row_list = [0 for col in range(cols)]
    array = [row_list for row in range(rows)]

    return array


if __name__ == "__main__":
    rows = 4
    cols = 5
    print(array_of_zeros(rows, cols))
