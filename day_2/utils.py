def factorization(
    num: int,
    ignore_trivial: bool = True
) -> list[tuple[int, int]]:
    """
    Determine all pairs of integers that multiply to this number.
    
    For example:
    - 7 -> [(1,7)] ([] if ignore_trivial)
    - 8 -> [(1,8),(2,4),(4,2)] ([(2,4),(4,2)] if ignore_trivial)
    """
    pairs: list[tuple[int, int]] = []

    for i in range(1, num // 2 + 1):
        if num % i == 0:
            quotient = int(num / i)
            pairs.append((i, quotient))
    
    if ignore_trivial:
        pairs.remove((1, num))

    return pairs


def create_split_list(
    num: int,
    split: tuple[int, int]
) -> list[int]:
    """
    Given an integer and `split` tuple, create a list of integers representing that number split.
    The tuple `split` encodes `item_length, n_items`.

    For example:
    - 11, (1, 2) -> [1, 1]
    - 123456, (2, 3) -> [12, 34, 56]
    """
    split_indices = _get_split_indices(num, split)
    num_as_str = str(num)

    split_list: list[int] = []

    for i in range(len(split_indices) - 1):
        idx_this = split_indices[i]
        idx_next = split_indices[i + 1]
        split_num = int(num_as_str[idx_this:idx_next])
        split_list.append(split_num)

    return split_list


def _get_split_indices(
    num: int,
    split: tuple[int, int]
) -> list[int]:
    """
    Given an integer and `split` tuple, create a list of indices to use for splitting.

    For example:
    - 11, (1, 2) -> [0, 1, 2]
    - 123456, (2, 3) -> [0, 2, 4, 6]
    """
    indices: list[int] = []

    num_len = len(str(num))

    for i in range(0, num_len, split[0]):
        indices.append(i)

    indices.append(num_len)

    return indices


def all_identical(
    split_list: list[int],
) -> bool:
    """
    Return True if all list items are identical, otherwise False.
    """
    return len(set(split_list)) == 1


if __name__ == "__main__":
    tests = [
        (11, (1, 2)),
        (123456, (2, 3))
    ]
    for test in tests:
        result = create_split_list(test[0], test[1])
        print(f"{test} -> {result}")