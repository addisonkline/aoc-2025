from utils import (
    get_line_target,
    get_line_buttons,
    get_line_jrs,
    create_target_vector,
    create_initial_vector,
    create_button_vector,
    vecmult,
    veccmp,
    vecstr,
    Matrix
)


class LightMachine:

    def __init__(
        self,
        targets: list[list[bool]],
        buttons: list[list[list[int]]],
        joltage_requirements: list[list[int]],
    ) -> None:
        self.targets = targets
        self.buttons = buttons
        self.joltage_requirements = joltage_requirements

        self._build_initial_state()

    def _build_initial_state(
        self,
    ) -> None:
        self.state = [(False for _ in self.targets[i]) for i in range(len(self.targets))]

    @staticmethod
    def from_string(
        input_str: str
    ) -> "LightMachine":
        """
        Create a LightMachine from the given input string (see `day_10/input.txt`).
        """
        lines = input_str.splitlines()
        targets: list[list[bool]] = []
        buttons: list[list[list[int]]] = []
        joltage_requirements: list[list[int]] = []

        for line in lines:
            line_target_str = line.split("]")[0].removeprefix("[")
            line_buttons_str = line.split("]")[1].split("{")[0]
            line_jrs_str = line.split("{")[1].removesuffix("}")

            line_target = get_line_target(line_target_str)
            line_buttons = get_line_buttons(line_buttons_str)
            line_jrs = get_line_jrs(line_jrs_str)

            targets.append(line_target)
            buttons.append(line_buttons)
            joltage_requirements.append(line_jrs)

        return LightMachine(
            targets=targets,
            buttons=buttons,
            joltage_requirements=joltage_requirements
        )
    
    def find_fewest_presses(
        self,
    ) -> tuple[list[list[list[int]]], int]:
        """
        Determine the fewest number of button presses to reach the target for each row.
        Returns `button_presses_by_row, total_button_presses`.
        """
        button_presses_per_row: list[list[list[int]]] = []
        total_button_presses = 0

        for i in range(len(self.targets)):
            print(f"on row {i}")
            target = self.targets[i]
            buttons = self.buttons[i]
            target_vec = create_target_vector(target)
            target_vec_size = len(target_vec)
            initial_vec = create_initial_vector(target_vec_size)
            button_vecs = [create_button_vector(button, target_vec_size) for button in buttons]

            print(f"target vec: {vecstr(target_vec)}")
            print(f"button vecs: {[vecstr(vec) for vec in button_vecs]}")

            button_matrix = Matrix(button_vecs)
            print(f"button matrix: \n{button_matrix}")
            button_matrix.gaussian_elimination()
            print(f"after GE: \n{button_matrix}")

        return button_presses_per_row, total_button_presses


if __name__ == "__main__":
    filepath = "day_10/input_test.txt"
    with open(filepath) as file:
        contents = file.read()
        lm = LightMachine.from_string(contents)
        button_presses_per_row, total_button_presses = lm.find_fewest_presses()
        print("=" * 80)
        print(f"total button presses: {total_button_presses}")