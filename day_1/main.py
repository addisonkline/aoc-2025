from typing import Literal

class Dial:
    """
    A dial that can be rotated left or right between 0 and 99.
    """

    def __init__(self) -> None:
        self.loc = 50

    def turn(
        self,
        direction: Literal["L", "R"],
        magnitude: int
    ) -> None:
        match direction:
            case "L":
                loc_new = self.loc - magnitude
            case "R":
                loc_new = self.loc + magnitude
        
        loc_mod_100 = loc_new % 100
        self.loc = loc_mod_100

    def process_input(
        self,
        input_filepath: str
    ) -> int:
        """
        Process a text file and return the number of times the dial is at 0 after a rotation.
        """
        with open(input_filepath) as file:
            lines = file.readlines()

            num_zeros = 0
            for line in lines:
                direction = line[0]
                assert (direction == "L" or direction == "R")
                magnitude = int(line[1:])
                self.turn(direction, magnitude) # type: ignore
                if self.loc == 0:
                    num_zeros += 1
        
            return num_zeros
        

if __name__ == "__main__":
    file = "day_1/input.txt"
    dial = Dial()
    num_zeros = dial.process_input(file)
    print(f"found {num_zeros} zeros in {file}")