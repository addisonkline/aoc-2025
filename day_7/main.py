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
    ) -> tuple[list[list[str]], int]:
        """
        Run the beam from the given manifold diagram.
        Returns `diagram_with_beam, final_num_beams`.
        """
        diagram_curr = self.diagram

        line_first = diagram_curr[0]
        cols = len(line_first)

        num_splits = 0

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
                        else:
                            print(f"beam continuing down")
                            diagram_curr[i][j] = "|"
                    case "^":
                        pass
                    case ".":
                        pass
                    case _:
                        raise ValueError(f"illegal character in diagram: {char}")

        return diagram_curr, num_splits


if __name__ == "__main__":
    filepath = "day_7/input.txt"
    with open(filepath) as file:
        contents = file.read()
        tm = TachyonManifold.from_string(contents)
        diagram, count = tm.run_beam()
        print("=" * 80)
        for line in diagram:
            print(line)
        print("-" * 80)
        print(f"final number of splits: {count}")