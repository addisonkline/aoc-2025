from utils import (
    factorization,
    create_split_list,
    all_identical
)


class Range:

    def __init__(
        self,
        lower: int,
        upper: int
    ) -> None:
        self.lower = lower
        self.upper = upper

    @staticmethod
    def from_str(
        string: str
    ) -> "Range":
        """
        Build a Range object from a string with format `lower-upper`.
        """
        lower_str, upper_str = string.split("-", maxsplit=1)
        lower = int(lower_str)
        upper = int(upper_str)

        return Range(lower, upper)

    def get_invalid_ids(
        self
    ) -> list[int]:
        """
        Determine all invalid ID numbers in this range and return them in a list.
        """
        invalid_ids: list[int] = []

        for id in range(self.lower, self.upper + 1):
            if not self._id_is_valid(id):
                invalid_ids.append(id)

        return invalid_ids
    
    def _id_is_valid(
        self,
        id: int
    ) -> bool:
        """
        Return True if the given ID is valid, otherwise False.
        """
        num_digits = len(str(id))
        
        possible_splits = factorization(num_digits, ignore_trivial=False)
        for s in possible_splits:
            if not s[1] == 2:
                continue
            split_list = create_split_list(id, s)
            if all_identical(split_list):
                return False

        return True


if __name__ == "__main__":
    filepath = "day_2/input.txt"
    with open(filepath) as file:
        contents = file.read()

        invalid_sum = 0
        for range_str in contents.split(","):
            r = Range.from_str(range_str)
            invalid_ids = r.get_invalid_ids()
            print(f"found {len(invalid_ids)} invalid IDs in range {range_str}: {invalid_ids}")
            for invalid_id in invalid_ids:
                invalid_sum += invalid_id
        
        print("=" * 80)
        print(f"sum of all invalid IDs: {invalid_sum}")