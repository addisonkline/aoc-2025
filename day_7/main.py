class TachyonManifold:

    def __init__(
        self,
        diagram: list[list[str]],
    ) -> None:
        self.diagram = diagram

    @staticmethod
    def from_string(
        input_str: str,
    ) -> "TachyonManifold":
        """
        Build a new TachyonManifold from the raw string input (see `day_7/input.txt`).
        """
        lines = input_str.splitlines()
        result: list[list[str]] = []
        for line in lines:
            line_lst = [char for char in line]
            result.append(line_lst)

        return TachyonManifold(
            diagram=result
        )
    
    def run_beam(
        self,
    ) -> tuple[list[list[str]], int, int]:
        """
        Run the beam from the given manifold diagram.
        Returns `diagram_with_beam, final_num_beams, final_num_timelines`.
        """
        diagram_curr = self.diagram

        line_first = diagram_curr[0]
        cols = len(line_first)

        num_splits = 0
        num_timelines = 0

        for i in range(1, len(self.diagram)):
            line_prev = diagram_curr[i - 1]

            for j in range(cols):
                char = line_prev[j]

                match char:
                    case "S":
                        print(f"found entrypoint S at {j},{i}")
                        diagram_curr[i][j] = "|"
                    case "|":
                        if diagram_curr[i][j] == "^": # beam is encountering a splitter
                            print(f"beam found splitter at {j},{i}, splitting")
                            diagram_curr[i][j - 1] = "|"
                            diagram_curr[i][j + 1] = "|"
                            num_splits += 1
                            num_timelines += 2
                        else:
                            print(f"beam continuing down")
                            diagram_curr[i][j] = "|"
                    case "^":
                        pass
                    case ".":
                        pass
                    case _:
                        raise ValueError(f"illegal character in diagram: {char}")
                    
        for i in range(1, len(self.diagram)):
            for j in range(1, cols - 1):
                if (diagram_curr[i][j - 1] == "^") and (diagram_curr[i][j] == "|") and (diagram_curr[i][j + 1] == "^"):
                    num_timelines -= 1

        return diagram_curr, num_splits, num_timelines
    
    def count_timelines(
        self,
    ) -> int:
        """
        Determine the number of possible timelines for this configuration.
        """
        raise NotImplementedError
    
    def _timelines_in_line(
        self,
        line: list[str]
    ) -> int:
        """
        Count the number of timelines in this row.
        """
        line_result = line

        for i in range(0, len(line)):
            if i == 0:
                if line[i + 1] == "^":
                    line_result[i] = "|"
                continue
            if i == len(line) - 1:
                if line[i - 1] == "^":
                    line_result[i] = "|"
                continue
            if (line[i - 1] == "^") or (line[i + 1] == "^"):
                line_result[i] = "|"
        
        return line_result.count("|")


if __name__ == "__main__":
    filepath = "day_7/input_test.txt"
    with open(filepath) as file:
        contents = file.read()
        tm = TachyonManifold.from_string(contents)
        diagram, num_splits, num_timelines = tm.run_beam()
        print("=" * 80)
        for line in diagram:
            print(line)
        print("-" * 80)
        print(f"final number of timelines: {num_timelines}")