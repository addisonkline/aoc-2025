from typing import Literal

class Dial:
    """
    A dial that can be rotated left or right between 0 and 99.
    """

    def __init__(self) -> None:
        self.loc = 50

    def _turn(
        self,
        direction: Literal["L", "R"],
        magnitude: int
    ) -> int:
        """
        Turn the dial left or right by the given magnitude.
        Returns the number of times this turn "crosses" 0.
        """
        loc_old = self.loc

        match direction:
            case "L":
                loc_new = loc_old - magnitude
            case "R":
                loc_new = loc_old + magnitude

        loc_mod_100 = loc_new % 100
        self.loc = loc_mod_100

        return self._num_clicks(loc_old, magnitude, direction)
    
    def _num_clicks(
        self,
        loc_start: int,
        magnitude: int,
        direction: Literal["L", "R"]
    ) -> int:
        """
        Count the number of times this turn crosses 0 on the dial.
        """
        crosses = 0

        match direction:
            case "L":
                loc_end = loc_start - magnitude
                for i in range(loc_start - 1, loc_end - 1, -1):
                    if i % 100 == 0:
                        crosses += 1
            case "R":
                loc_end = loc_start + magnitude
                for i in range(loc_start + 1, loc_end + 1, 1):
                    if i % 100 == 0:
                        crosses += 1
                
        return crosses

    def process_input(
        self,
        input_filepath: str
    ) -> int:
        """
        Process a text file and return the number of times the dial is at 0 after a rotation.
        """
        with open(input_filepath) as file:
            lines = file.readlines()

            clicks = 0
            for line in lines:
                direction = line[0]
                assert (direction == "L" or direction == "R")
                magnitude = int(line[1:])
                clicks_this = self._turn(direction, magnitude) # type: ignore
                print(f"{direction}{magnitude} to {self.loc}, clicks = {clicks_this}")
                clicks += clicks_this
        
            return clicks
        

if __name__ == "__main__":
    file = "day_1/input.txt"
    dial = Dial()
    num_zeros = dial.process_input(file)
    print(f"found {num_zeros} zeros in {file}")