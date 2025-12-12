class ServerRack:

    def __init__(
        self,
        devices: dict[str, list[str]]
    ) -> None:
        self.devices = devices

    @staticmethod
    def from_string(
        input_str: str,
    ) -> "ServerRack":
        """
        Create a ServerRack from the raw string input (see `day_11/input.txt`).
        """
        devices: dict[str, list[str]] = {}
        lines = input_str.splitlines()

        for line in lines:
            key, values = line.split(": ", maxsplit=1)
            values_lst = values.split(" ")
            devices[key] = values_lst

        return ServerRack(
            devices=devices
        )
    
    def find_paths(
        self,
        start: str,
        end: str,
    ) -> tuple[list[list[str]], int]:
        """
        Find the number of paths between `start` and `end`.
        Returns `list_of_paths, number_of_paths`.
        """
        list_of_paths: list[list[str]] = []
        number_of_paths = 0

        values = self.devices[start]
        print(f"values: {values}")
        for value in values:
            if value == end:
                list_of_paths.append([start, end])
                number_of_paths += 1
            else:
                values.extend(self.devices[value])

        return list_of_paths, number_of_paths
    
    def find_paths_through(
        self,
        start: str,
        end: str,
        through: list[str],
    ) -> int:
        """
        Find the number of paths between `start` and `end` that include everything in `through`.
        """
        raise NotImplementedError


if __name__ == "__main__":
    filepath = "day_11/input_test_p2.txt"
    with open(filepath) as file:
        contents = file.read()
        sr = ServerRack.from_string(contents)
        number_of_paths = sr.find_paths_through("svr", "out", ["dac", "fft"])
        print("=" * 80)
        print(f"number of paths: {number_of_paths}")
