from utils import (
    find_all_occurrences,
    first_unique_pairing,
    largest_digit_in_interval
)

class BatteryBank:

    def __init__(
        self,
        joltages: list[int],
        subsize: int = 12,
    ) -> None:
        self.joltages = joltages
        self.subsize = subsize

    @staticmethod
    def from_string(
        input_str: str
    ) -> "BatteryBank":
        """
        Build a BatteryBank from a string of joltages (e.g. 987654321111111).
        """
        joltages: list[int] = []
        for i in range(len(input_str)):
            joltages.append(int(input_str[i]))

        return BatteryBank(joltages)
    
    def max_joltage(
        self,
    ) -> tuple[int, list[int]]:
        """
        Obtain the max joltage (ordered n-tuple with the largest value).
        Returns `max_joltage, indices`.
        """
        max_joltage_str = ""
        indices: list[int] = []
        idx_start = 0
        idx_end = len(self.joltages) - self.subsize + 1

        for _ in range(self.subsize):
            digit_val, digit_loc = largest_digit_in_interval(self.joltages, idx_start, idx_end)
            max_joltage_str += str(digit_val)
            indices.append(digit_loc)
            idx_start = digit_loc + 1
            idx_end += 1

        return int(max_joltage_str), indices
    

if __name__ == "__main__":
    filepath = "day_3/input.txt"
    with open(filepath) as file:
        joltage_sum = 0
        for line in file.readlines():
            line = line.removesuffix("\n")
            bb = BatteryBank.from_string(line)
            max_joltage, indices = bb.max_joltage()
            print(f"{line} -> {max_joltage} from {indices}")
            joltage_sum += max_joltage
        print("=" * 80)
        print(f"sum of all joltages: {joltage_sum}")