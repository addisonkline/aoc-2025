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

    
if __name__ == "__main__":
    filepath = "day_4/input.txt"
    with open(filepath) as file:
        contents = file.read()
        pr = PaperRolls.from_string(contents)
        num_rolls, _ = pr.accessible_rolls()
        print("=" * 80)
        print(f"number of accessible rolls: {num_rolls}")