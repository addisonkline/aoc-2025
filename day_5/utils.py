def condense_ranges(
    r1: tuple[int, int],
    r2: tuple[int, int],
) -> tuple[int, int] | None:
    """
    Condense the given ranges into a single one if they overlap.
    If no overlap exists, return `None`.
    """
    r1_start = r1[0]
    r1_end = r1[1]
    r2_start = r2[0]
    r2_end = r2[1]

    # case 1: r1 starts before r2
    if (r1_start < r2_start) and (r1_end <= r2_end) and (r1_end > r2_start):
        return (r1_start, r2_end)
    # case 2: r1 starts after r2
    if (r1_start > r2_start) and (r1_end >= r2_end) and (r2_start > r1_end):
        return (r2_start, r1_end)
    # case 3: r1 contains r2
    if (r1_start < r2_start) and (r1_end > r2_end):
        return  (r1_start, r1_end)
    # case 4: r2 contains r1
    if (r2_start < r1_start) and (r2_end > r1_end):
        return (r2_start, r2_end)
    # case 5: ranges are identical
    if (r1_start == r2_start) and (r1_end == r2_end):
        return (r1_start, r1_end)

    # no overlap
    return None