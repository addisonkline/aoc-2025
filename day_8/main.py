import math

class BoxNetwork:

    def __init__(
        self,
        boxes: list[tuple[int, int, int]]
    ) -> None:
        self.boxes = boxes

    @staticmethod
    def from_string(
        input_str: str,
    ) -> "BoxNetwork":
        lines = input_str.splitlines()

        boxes: list[tuple[int, int, int]] = []
        for line in lines:
            coords = line.split(",")

            if not len(coords) == 3:
                raise ValueError(f"illegal coordinate size: {len(coords)}")
            
            box = (int(coords[0]), int(coords[1]), int(coords[2]))
            boxes.append(box)
        
        return BoxNetwork(
            boxes=boxes
        )
    
    def connect_n_nearest_boxes(
        self,
        n: int,
    ) -> list[list[tuple[int, int, int]]]:
        self.calculate_distances()

        n_shortest_distances = self.find_n_shortest_distances(n)

        print(f"{n} shortest distances: {n_shortest_distances}")

        raise NotImplementedError
    
    def calculate_distances(
        self,
    ) -> None:
        distances: dict[tuple[int, int], float] = {}

        for i in range(len(self.boxes)):
            for j in range(i + 1, len(self.boxes)):
                box_outer = self.boxes[i]
                box_inner = self.boxes[j]
                x1, y1, z1 = box_outer
                x2, y2, z2 = box_inner
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
                distances[(i, j)] = distance

        self.distances = distances
    
    def find_n_shortest_distances(
        self,
        n: int,
    ) -> list[tuple[int, int]]:
        """
        Return the indices of the N shortest distances in this network.
        """
        n_shortest: list[tuple[int, int]] = []

        for i in range(n):
            shortest = 2.0 ** 32
            shortest_j, shortest_k = 0, 0

            for j in range(len(self.boxes)):
                for k in range(j + 1, len(self.boxes)):
                    if self.distances[(j, k)] < shortest:
                        if (j, k) in n_shortest:
                            continue
                        shortest = self.distances[(j, k)]
                        shortest_j = j
                        shortest_k = k
            
            n_shortest.append((shortest_j, shortest_k))
        
        return n_shortest
            

if __name__ == "__main__":
    filepath = "day_8/input_test.txt"
    with open(filepath) as file:
        contents = file.read()
        bn = BoxNetwork.from_string(contents)
        circuits = bn.connect_n_nearest_boxes(10)
        print("=" * 80)
        print(bn.boxes)