from fractions import Fraction

Vector = list[int]

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
    return [(1 if t else 0) for t in target]


def create_initial_vector(
    size: int,
) -> Vector:
    """
    Create an initial state vector of the given size (all entries are -1).
    """
    return [0 for _ in range(size)]


def create_button_vector(
    button: list[int],
    size: int,
) -> Vector:
    """
    Given a button and target size, create a vector of 1 and -1.
    """
    return [(1 if i in button else 0) for i in range(size)]


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
    
    return [(1 if v1[i] == v2[i] else 0) for i in range(len(v1))]


class Matrix:

    def __init__(
        self,
        vectors: list[list[Fraction]]
    ) -> None:
        self.values = [vectors]

    @staticmethod
    def identity(
        size: int,
    ) -> "Matrix":
        """
        Return an identity matrix with the given size.
        """
        vectors = [[(Fraction(1) if row == col else Fraction(0)) for col in range(size)] for row in range(size)]

        return Matrix(
            vectors=vectors
        )

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
        
        inverse = self._gaussian_elimination()

        return inverse
    
    def _gaussian_elimination(
        self,
    ) -> "Matrix":
        """
        Perform Gaussian elimination on this matrix and return the calculated inverse.
        """
        primary = Matrix(self.values)
        augmented = self.identity(len(primary))

        raise NotImplementedError


        
