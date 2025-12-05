from utils import (
    get_adjacent_indices,
    num_true
)

class PaperRolls:

    def __init__(
        self,
        num_rows: int,
        num_cols: int,
        rolls: list[list[bool]],
    ) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.rolls = rolls

    @staticmethod
    def from_string(
        input_str: str,
    ) -> "PaperRolls":
        """
        Build a PaperRolls object from raw string input (e.g. `..@@.@@@@.`).
        """
        rolls: list[list[bool]] = []

        lines = input_str.splitlines()
        for line in lines:
            row: list[bool] = []
            for char in line:
                match char:
                    case "@":
                        row.append(True)
                    case ".":
                        row.append(False)
                    case _:
                        raise ValueError(f"unexpected character: {char}")
            
            rolls.append(row)
        
        return PaperRolls(
            num_rows=len(rolls),
            num_cols=len(rolls[0]),
            rolls=rolls
        )
    
    def accessible_rolls(
        self,
        threshold: int = 4,
    ) -> tuple[int, list[tuple[int, int]]]:
        """
        Find all paper rolls accessible by a forklift (< `threshold` rolls in adjacent spots).
        Returns `num_rolls, indices_rolls`.
        """
        num_rolls = 0
        indices_rolls: list[tuple[int, int]] = []

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if not self.rolls[row][col]:
                    # not worth checking spots that are not rolls
                    continue

                adjacents = get_adjacent_indices(row, col, self.num_rows, self.num_cols)
                num_adjacent_rolls = num_true(self.rolls, adjacents)
                if (num_adjacent_rolls < threshold):
                    print(f"roll at {row},{col} is accessible: {num_adjacent_rolls} found among {len(adjacents)} adjacent spots")
                    num_rolls += 1
                    indices_rolls.append((row, col))

        return num_rolls, indices_rolls
    
    def remove_rolls(
        self,
        coords: list[tuple[int, int]]
    ) -> None:
        """
        Remove the paper rolls at all spots in the specified list of coordinates.
        """
        for row, col in coords:
            self.rolls[row][col] = False

    def remove_rolls_iterative(
        self,
    ) -> tuple[int, list[list[tuple[int, int]]]]:
        """
        Iteratively remove all rolls in this array until none are left.
        Returns `num_rolls_removed, removal_coords_by_iteration`.
        """
        num_rolls_removed = 0
        rcs: list[list[tuple[int, int]]] = []

        accessible_num, accessible_coords = self.accessible_rolls()
        while accessible_num > 0:
            self.remove_rolls(accessible_coords)
            print(f"found and removed {accessible_num} rolls")
            num_rolls_removed += accessible_num
            rcs.append(accessible_coords)

            accessible_num, accessible_coords = self.accessible_rolls()
        
        return num_rolls_removed, rcs

    
if __name__ == "__main__":
    filepath = "day_4/input.txt"
    with open(filepath) as file:
        contents = file.read()
        pr = PaperRolls.from_string(contents)
        num_rolls_removed, rcs = pr.remove_rolls_iterative()
        print("=" * 80)
        print(f"removals complete after {len(rcs)} iterations")
        print(f"number of removed rolls: {num_rolls_removed}")
