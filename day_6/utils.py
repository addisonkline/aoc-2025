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
    row_list = [0 for _ in range(cols)]
    array = [row_list for _ in range(rows)]

    return array


def build_number_strings_lists(
    file_content: str,
) -> list[list[str]]:
    """
    Given raw text contents, build a list of number columns as a `list[list[str]]`.
    """
    lines = file_content.splitlines()
    line_first = lines[0]

    # find the indices of every split inside each row
    num_exists_in_col = [False for char in line_first]
    for line in lines:
        for i in range(len(line)):
            if not line[i] == " ":
                num_exists_in_col[i] = True

    split_indices = [0]
    split_indices.extend([i for i in range(len(num_exists_in_col)) if not num_exists_in_col[i]])
    split_indices.append(len(line_first))
    print(f"split indices: {split_indices}")

    # split each line by the split indices
    str_arr: list[list[str]] = []

    for line in lines:
        str_lst: list[str] = []
        for i in range(len(split_indices) - 1):
            idx_start = split_indices[i] + 1 if not i == 0 else split_indices[i]
            idx_end = split_indices[i + 1] + 1 if not i == 0 else split_indices[i + 1]
            value = line[idx_start:idx_end]
            str_lst.append(value)
        
        print(f"{line} -> {str_lst}")
        str_arr.append(str_lst)

    # return final str columns
    str_arr_final: list[list[str]] = []
    for col in range(len(str_arr[0])):
        str_col = [row[col] for row in str_arr]
        str_arr_final.append(str_col)

    return str_arr_final


def parse_cephalopod_numbers(
    l: list[str],
) -> list[int]:
    """
    Rebuild a list of numbers in cephalopod format (right-to-left in columns).

    For example:
    - [64, 23, 314] -> [4, 431, 623]
    """
    max_len = 0
    for i in range(len(l)):
        len_this = len(l[i])
        if len_this > max_len:
            max_len = len_this
    
    print(f"list {l} has max item length {max_len}")

    parsed: list[int] = []
    for i in range(max_len - 1, -1, -1):
        parsed_this = ""
        for num in l:
            try:
                num_as_str = str(num)
                parsed_this += num_as_str[i]
            except IndexError:
                continue
        if parsed_this.strip() == "":
            continue
        
        parsed.append(int(parsed_this))

    return parsed


if __name__ == "__main__":
    filepath = "day_6/input_test.txt"
    with open(filepath) as file:
        contents = file.read()
        result = build_number_strings_lists(contents)
        numbers = result[0]
        numbers = numbers[:-1]
        print(numbers)
        print(parse_cephalopod_numbers(numbers))
