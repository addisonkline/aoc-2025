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

        count = 0
        for start, end in self.ranges:
            count += end - start + 1

        return count
    
    def _merge_ranges(
        self,
        max_iters: int = 10
    ) -> None:
        """
        Iteratively condense the ranges provided to remove overlap.
        """
        iteration = 0
        done = False

        while not done:
            print(f"ranges at iteration {iteration}: {self.ranges}")
            num_merges = 0
            temp_ranges: list[tuple[int, int]] = []
            mergeable: dict[tuple[int, int], bool] = {(start, stop): False for start, stop in self.ranges}

            for i in range(len(self.ranges)):
                for j in range(i + 1, len(self.ranges)):
                    condensed = condense_ranges(self.ranges[i], self.ranges[j])

                    # these items can be merged
                    if condensed is not None:
                        print(f"merging: {self.ranges[i]} + {self.ranges[j]} -> {condensed}")
                        temp_ranges.append(condensed)
                        mergeable[self.ranges[i]] = True
                        mergeable[self.ranges[j]] = True
                        num_merges += 1

            print(f"after iteration {iteration}:")
            print(f"temp: {temp_ranges}")
            print(f"mergeables: {mergeable}")

            # create final ranges list for this cycle
            unmergeables = [key for key, val in mergeable.items() if not val]
            final = unmergeables + list(set(temp_ranges))

            iteration += 1
            self.ranges = final

            if num_merges == 0:
                done = True

            if iteration == max_iters:
                break
            

if __name__ == "__main__":
    filepath = "day_5/input.txt"
    with open(filepath) as file:
        contents = file.read()
        idb = IngredientDB.from_string(contents)
        num_fresh = idb.count_fresh_ids()
        print("=" * 80)
        print(f"number of fresh ingredient IDs: {num_fresh}")