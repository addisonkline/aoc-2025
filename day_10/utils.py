from fractions import Fraction

Vector = list[Fraction]

def get_line_target(
    line_str: str
) -> list[bool]:
    """
    Convert a raw string into a target (list of bools).
    """
    target: list[bool] = []

    for char in line_str:
        match char:
            case "#":
                target.append(True)
            case ".":
                target.append(False)
            case _:
                raise ValueError(f"illegal character: {char}")
            
    return target


def get_line_buttons(
    line_str: str
) -> list[list[int]]:
    """
    Convert a raw string into a list of buttons (list of list of ints).
    """
    buttons: list[list[int]] = []
    buttons_lst = line_str.split(")")

    for button_str in buttons_lst:
        button_nums: list[int] = []
        for char in button_str:
            try:
                num = int(char)
                button_nums.append(num)
            except Exception:
                continue
        
        buttons.append(button_nums)

    return buttons[:-1] # the last entry is an empty list


def get_line_jrs(
    line_str: str
) -> list[int]:
    """
    Convert a raw string into a list of joltage requirements (list of ints).
    """
    jrs: list[int] = []
    line_jrs_str = line_str.split(",")

    for num_str in line_jrs_str:
        try:
            num = int(num_str)
            jrs.append(num)
        except Exception:
            raise ValueError(f"illegal value: {num_str}")
        
    return jrs


def create_target_vector(
    target: list[bool]
) -> Vector:
    """
    Turn a list of boolean values into a vector of 1 and -1.
    """
    return [(Fraction(1) if t else Fraction(0)) for t in target]


def create_initial_vector(
    size: int,
) -> Vector:
    """
    Create an initial state vector of the given size (all entries are -1).
    """
    return [Fraction(0) for _ in range(size)]


def create_button_vector(
    button: list[int],
    size: int,
) -> Vector:
    """
    Given a button and target size, create a vector of 1 and -1.
    """
    return [(Fraction(1) if i in button else Fraction(0)) for i in range(size)]


def vecmult(
    v1: Vector,
    v2: Vector,
) -> Vector:
    """
    Multiply the two given vectors together.
    The two vectors must be the same length.
    """
    if not len(v1) == len(v2):
        raise ValueError(f"the two vectors must have equal length: got {len(v1)} and {len(v2)}")
    
    return [v1[i] * v2[i] for i in range(len(v1))]


def vecadd(
    v1: Vector,
    v2: Vector,
) -> Vector:
    """
    Add the two given vectors together.
    The two vectors must be the same length.
    """
    if not len(v1) == len(v2):
        raise ValueError(f"the two vectors must have equal length: got {len(v1)} and {len(v2)}")
    
    return [v1[i] + v2[i] for i in range(len(v1))]


def veccmp(
    v1: Vector,
    v2: Vector,
) -> Vector:
    """
    Return a vector with 1 where the two vectors have equal elements, -1 otherwise.
    The two vectors must be the same length.
    """
    if not len(v1) == len(v2):
        raise ValueError(f"the two vectors must have equal length: got {len(v1)} and {len(v2)}")
    
    return [(Fraction(1) if v1[i] == v2[i] else Fraction(0)) for i in range(len(v1))]


def vecstr(
    v: Vector,
) -> str:
    """
    Create a legible string representation for the given vector.
    """
    result = "["
    for frac in v:
        result += frac.__str__()
        result += ", "
    result += "]"

    return result


def vecargmax(
    v: Vector,
    idx_start: int,
    idx_end: int,
) -> int:
    """
    Find the index of this vector with the maximum value between `idx_start` and `idx_end`.
    """
    if (idx_start < 0) or (idx_start > len(v) - 1):
        raise ValueError(f"idx_start must be between 0 and {len(v) - 1}, got {idx_start}")
    if (idx_end < 0) or (idx_end > len(v) - 1):
        raise ValueError(f"idx_end must be between 0 and {len(v) - 1}, got {idx_end}")

    idx_max = idx_start

    for i in range(idx_start, idx_end + 1):
        if v[i] > v[idx_max]:
            idx_max = i

    return i


def vecabs(
    v: Vector,
) -> Vector:
    """
    Return the absolute value of this vector.
    """
    return [abs(vec) for vec in v]


class Matrix:

    def __init__(
        self,
        col_vectors: list[Vector]
    ) -> None:
        self.values = [list(row) for row in zip(*col_vectors)]
        self.rows = len(col_vectors[0])
        self.cols = len(col_vectors)

    def __repr__(
        self,
    ) -> str:
        result = ""
        for line in self.values:
            line_result = vecstr(line)
            result += line_result
            result += "\n"

        return result

    @staticmethod
    def identity(
        size: int,
    ) -> "Matrix":
        """
        Return an identity matrix with the given size.
        """
        vectors = [[(Fraction(1) if row == col else Fraction(0)) for col in range(size)] for row in range(size)]

        return Matrix(
            col_vectors=vectors
        )
    
    def is_identity(
        self,
    ) -> bool:
        """
        Determine if this matrix is a valid identity matrix.
        """
        if not self.rows == self.cols:
            return False
        
        for row in range(self.rows):
            for col in range(self.cols):
                if row == col:
                    if not self.values[row][col] == 1:
                        return False
                else:
                    if not self.values[row][col] == 0:
                        return False
                    
        return True
    
    def get_val(
        self,
        row: int,
        col: int,
    ) -> Fraction:
        """
        Get the matrix's value at `row, col`.
        """
        if (row >= self.rows) or (row < 0):
            raise ValueError(f"row must be between 0 and {self.rows - 1}, got {row}")
        if (col >= self.cols) or (col < 0):
            raise ValueError(f"col must be between 0 and {self.cols - 1}, got {col}")

        return self.values[row][col]
    
    def set_val(
        self,
        row: int,
        col: int,
        value: Fraction,
    ) -> None:
        """
        Set the matrix's value at `row, col`.
        """
        if (row >= self.rows) or (row < 0):
            raise ValueError(f"row must be between 0 and {self.rows - 1}, got {row}")
        if (col >= self.cols) or (col < 0):
            raise ValueError(f"col must be between 0 and {self.cols - 1}, got {col}")
        
        self.values[row][col] = value
    
    def get_row(
        self,
        row: int,
    ) -> Vector:
        """
        Get this matrix's row at the given index.
        """
        if (row < 0) or (row >= self.rows):
            raise ValueError(f"row must be between 0 and {self.rows - 1}, got {row}")

        return self.values[row][:]
    
    def set_row(
        self,
        row_idx: int,
        row_vec: Vector,
    ) -> None:
        """
        Set the row at the given index to the given row vector.
        """
        if (row_idx < 0) or (row_idx >= self.rows):
            raise ValueError(f"row must be between 0 and {self.rows - 1}, got {row_idx}")

        self.values[row_idx] = row_vec

    def swap_rows(
        self,
        idx_1: int,
        idx_2: int,
    ) -> None:
        """
        Swap this matrix's rows at `idx_1` and `idx_2`.
        """
        if (idx_1 < 0) or (idx_1 >= self.rows):
            raise ValueError(f"idx_1 must be between 0 and {self.rows - 1}, got {idx_1}")
        if (idx_2 < 0) or (idx_2 >= self.rows):
            raise ValueError(f"idx_2 must be between 0 and {self.rows - 1}, got {idx_2}")

        temp = self.values[idx_1]
        self.values[idx_1] = self.values[idx_2]
        self.values[idx_2] = temp

    def get_col(
        self,
        col_idx: int,
    ) -> Vector:
        """
        Get this matrix's column at the given index.
        """
        if (col_idx < 0) or (col_idx >= self.cols):
            raise ValueError(f"col_idx must be between 0 and {self.cols - 1}, got {col_idx}")

        return [self.values[i][col_idx] for i in range(self.rows)]
    
    def set_col(
        self,
        col_idx: int,
        col_vec: Vector,
    ) -> None:
        """
        Set the column at the given index to the given column vector.
        """
        if (col_idx < 0) or (col_idx >= self.cols):
            raise ValueError(f"col_idx must be between 0 and {self.cols - 1}, got {col_idx}")

        for i in range(self.rows):
            self.values[i][col_idx] = col_vec[i]

    def mult_before(
        self,
        other: "Matrix",
    ) -> "Matrix":
        """
        For this matrix `self` and given matrix `other`, return `self*other`.
        """
        raise NotImplementedError
    
    def mult_after(
        self,
        other: "Matrix",
    ) -> "Matrix":
        """
        For this matrix `self` and given matrix `other`, return `other*self`.
        """
        raise NotImplementedError

    def get_inverse(
        self
    ) -> "Matrix":
        """
        Return the inverse of this matrix.
        This matrix must be square to have an inverse.
        """
        rows = len(self.values)
        cols = len(self.values[0])

        if not rows == cols:
            raise ValueError(f"only square matrices have an inverse")
        
        raise NotImplementedError
    
    def transpose(
        self,
    ) -> None:
        """
        Transpose this matrix in-place.
        """
        col_vectors = self.values
        self.values = [list(row) for row in zip(*col_vectors)]
        self.rows = len(col_vectors[0])
        self.cols = len(col_vectors)

    
    def gaussian_elimination(
        self,
    ) -> None:
        """
        Perform Gaussian elimination on this matrix and return the result.
        """
        if self.rows > self.cols:
            self.transpose()

        # yoinked from wikipedia
        h = 0 # initialize pivot row
        k = 0 # initialize pivot col

        while (h < self.rows) and (k < self.cols):
            # find the k-th pivot
            i_max = vecargmax(vecabs(self.get_col(k)), h, self.rows - 1)
            if self.get_val(i_max, k) == Fraction(0):
                # no pivot in this column, pass to next column
                k += 1
            else:
                self.swap_rows(h, i_max)
                # do for all rows below pivot:
                for i in range(h + 1, self.rows):
                    f = self.get_val(i, k) / self.get_val(h, k)
                    # fill the lower part of the pivot column with zeros
                    self.set_val(i, k, Fraction(0))
                    # do for all remaining elements in current row:
                    for j in range(k + 1, self.cols):
                        result = self.get_val(i, j) - (self.get_val(h, j) * f)
                        self.set_val(i, j, result)
            
                # increase pivot row and column
                h += 1
                k += 1