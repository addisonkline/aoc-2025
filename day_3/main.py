from utils import (
    find_all_occurrences,
    first_unique_pairing
)

class BatteryBank:

    def __init__(
        self,
        joltages: list[int],
    ) -> None:
        self.joltages = joltages

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
    ) -> tuple[int, int, int]:
        """
        Obtain the max joltage (ordered pair with the largest value).
        Returns `max_joltage, index_first, index_last`.
        """
        max_joltage, index_first, index_last = 0, 0, 0

        for joltage_target in range(99, 1, -1):
            digit_tens = joltage_target // 10
            digit_ones = joltage_target % 10

            if digit_ones == 0: # multiples of 10 are impossible
                continue
            if digit_tens not in self.joltages: # if this digit doesn't exist, no point in checking
                continue
            if digit_ones not in self.joltages: # ditto
                continue

            indices_tens = find_all_occurrences(self.joltages, digit_tens)
            indices_ones = find_all_occurrences(self.joltages, digit_ones)
            
            if first_unique_pairing(indices_tens, indices_ones) is not None:
                index_first, index_last = first_unique_pairing(indices_tens, indices_ones)
                max_joltage = int(f"{digit_tens}{digit_ones}")
                break

        return max_joltage, index_first, index_last
    

if __name__ == "__main__":
    filepath = "day_3/input.txt"
    with open(filepath) as file:
        joltage_sum = 0
        for line in file.readlines():
            line = line.removesuffix("\n")
            bb = BatteryBank.from_string(line)
            max_joltage, index_0, index_1 = bb.max_joltage()
            print(f"{line} -> {max_joltage} from [{index_0};{index_1}]")
            joltage_sum += max_joltage
        print("=" * 80)
        print(f"sum of all joltages: {joltage_sum}")