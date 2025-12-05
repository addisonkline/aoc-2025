def find_all_occurrences(
    nums: list[int],
    digit: int
) -> list[int]:
    """
    Find all occurrences of the given digit in the given integer list.
    Returns a list of all indices where this digit exists.
    """
    indices: list[int] = []
    for i in range(len(nums)):
        num = nums[i]
        if num == digit:
            indices.append(i)

    return indices


def first_unique_pairing(
    list_first: list[int],
    list_second: list[int],
) -> tuple[int, int] | None:
    """
    Find the first unique pairing of indices from the given lists.
    Returns `idx_first, idx_second` if one exists, otherwise `None`.
    """
    if list_first == []:
        return None
    
    for i in range(len(list_second)):
        idx_second = list_second[i]
        if list_first[0] < idx_second:
            return 0, idx_second

    return None


def largest_digit_in_interval(
    l: list[int],
    idx_start: int,
    idx_end: int,
) -> tuple[int, int]:
    """
    Find the largest digit in a subrange of the given list.
    Returns `largest_digit, index_largest_digit`.
    """
    largest = 0
    idx = 0
    
    for i in range(idx_start, idx_end):
        digit = l[i]
        if digit > largest:
            largest = digit
            idx = i

    return largest, idx