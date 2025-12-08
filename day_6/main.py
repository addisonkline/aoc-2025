from dataclasses import dataclass
from enum import StrEnum

from utils import (
    product,
    array_of_zeros
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
        lines = input_str.splitlines()
        num_rows = len(lines) - 1
        num_cols = len(lines[0].split())

        int_arr = array_of_zeros(num_rows, num_cols)

        for i in range(num_rows):
            line = lines[i].split()
            int_row = [int(val) for val in line]
            int_arr[i] = int_row

        print(f"num table: {int_arr} ({len(int_arr)}x{len(int_arr[0])})")

        list_ops = MathWorksheet._handle_operations_row(lines[num_rows].split())

        print(f"list ops: {list_ops}")

        # create final lists
        final: list[MathProblem] = []
        for i in range(num_cols):
            nums = [row[i] for row in int_arr]
            op = list_ops[i]
            problem = MathProblem(
                numbers=nums,
                operation=op
            )
            final.append(problem)

        return MathWorksheet(
            problems=final
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
