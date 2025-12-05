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
    ) -> tuple[int, list[int]]:
        """
        Obtain the max joltage (ordered n-tuple with the largest value).
        Returns `max_joltage, indices`.
        """
        raise NotImplementedError # TODO: this
    

if __name__ == "__main__":
    filepath = "day_3/input_test.txt"
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