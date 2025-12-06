from utils import (
    condense_ranges
)


class IngredientDB:

    def __init__(
        self,
        ranges: list[tuple[int, int]],
        ids_to_check: list[int],
    ) -> None:
        self.ranges = ranges
        self.ids_to_check = ids_to_check

    @staticmethod
    def from_string(
        input_str: str,
    ) -> "IngredientDB":
        """
        Build an IngredientDB from an input string (e.g. `3-5\n10-14\n\n1\n5\n8`).
        """
        lines = input_str.splitlines()
        lines.remove("") # remove the space between ranges and IDs

        ranges_str = [line for line in lines if "-" in line]
        ids = [int(line) for line in lines if "-" not in line]

        ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges_str]

        return IngredientDB(
            ranges=ranges,
            ids_to_check=ids
        )
    
    def check_ids(
        self,
    ) -> int:
        """
        Count the number of fresh ingredients based on existing ranges and IDs to check.
        """
        count = 0

        for id in self.ids_to_check:
            for min, max in self.ranges:
                if (id >= min) and (id <= max):
                    print(f"ingredient with ID {id} is fresh: in range {min}-{max}")
                    count += 1
                    break
        
        return count
    
    def count_fresh_ids(
        self,
    ) -> int:
        """
        Count the number of possible fresh IDs based on the existing ranges.
        """
        self._merge_ranges()
        print(f"{len(self.ranges)} ranges after merging: {self.ranges}")

        raise NotImplementedError
    
    def _merge_ranges(
        self,
    ) -> None:
        """
        Iteratively condense the ranges provided to remove overlap.
        """
        overlap_exists = True
        current_ranges = self.ranges

        while overlap_exists:
            temp_ranges: list[tuple[int, int]] = []
            num_merges = 0
            print(f"current ranges: {current_ranges}")
            for i in range(len(current_ranges)):
                for j in range(i + 1, len(current_ranges)):
                    condensed = condense_ranges(current_ranges[i], current_ranges[j])
                    
                    raise NotImplementedError


if __name__ == "__main__":
    filepath = "day_5/input_test.txt"
    with open(filepath) as file:
        contents = file.read()
        idb = IngredientDB.from_string(contents)
        num_fresh = idb.count_fresh_ids()
        print("=" * 80)
        print(f"number of fresh ingredient IDs: {num_fresh}")