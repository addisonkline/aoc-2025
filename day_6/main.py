from dataclasses import dataclass
from enum import StrEnum

from utils import (
    product,
    array_of_zeros,
    build_number_strings_lists,
    parse_cephalopod_numbers
)

class OperationType(StrEnum):
    ADD = "+"
    MULTIPLY = "*"


@dataclass
class MathProblem:
    numbers: list[int]
    operation: OperationType

    def solve(
        self,
    ) -> int:
        """
        Solve this math problem and return the integer result.
        """
        match self.operation:
            case OperationType.ADD:
                result = sum(self.numbers)
            case OperationType.MULTIPLY:
                result = product(self.numbers)

        return result


class MathWorksheet:

    def __init__(
        self,
        problems: list[MathProblem]
    ) -> None:
        self.problems = problems

    @staticmethod
    def _handle_operations_row(
        input_row: list[str],
    ) -> list[OperationType]:
        """
        Handle an input row of only operation types (+ or *).
        """
        result: list[OperationType] = []

        for val in input_row:
            match val:
                case "+":
                    result.append(OperationType.ADD)
                case "*":
                    result.append(OperationType.MULTIPLY)
                case _:
                    raise ValueError(f"illegal operation type: {val}")
                
        return result
    
    @staticmethod
    def _handle_numbers_row(
        input_row: list[str],
    ) -> list[int]:
        """
        Handle an input row of only numbers (as strings).
        """
        result: list[int] = []

        for val in input_row:
            val_num = int(val)
            result.append(val_num)

        return result

    @staticmethod
    def from_string(
        input_str: str,
    ) -> "MathWorksheet":
        """
        Build a MathWorksheet from the given string input (see `day_6/input.txt`).
        """
        number_strings_arr = build_number_strings_lists(input_str)

        problems: list[MathProblem] = []

        for lst in number_strings_arr:
            nums = lst[:-1]
            print(nums)
            op = lst[-1]

            nums_adj = parse_cephalopod_numbers(nums)
            op_sanitized = op.strip()

            match op_sanitized:
                case "+":
                    op_enum = OperationType.ADD
                case "*":
                    op_enum = OperationType.MULTIPLY

            problem = MathProblem(
                numbers=nums_adj,
                operation=op_enum
            )

            problems.append(problem)
        
        return MathWorksheet(
            problems=problems
        )

    
    def solve_problems(
        self,
    ) -> list[int]:
        """
        Solve all MathProblems in this MathWorksheet.
        """
        results: list[int] = []

        for p in self.problems:
            res = p.solve()
            results.append(res)

        return results
    

if __name__ == "__main__":
    filepath = "day_6/input.txt"
    with open(filepath) as file:
        contents = file.read()
        mw = MathWorksheet.from_string(contents)
        print("=" * 80)
        print(f"sum of all results: {sum(mw.solve_problems())}")
