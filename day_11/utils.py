class DAG:
    """
    Basic directed acyclic graph.
    """

    def __init__(
        self,
        vertices: list[str],
        edges: list[tuple[str, str]]
    ) -> None:
        self.vertices = vertices
        self.edges = edges

    def get_children(
        self,
        vertex: str,
    ) -> list[str]:
        """
        Get the list of children of this vertex.
        """
        return [edge[1] for edge in self.edges if edge[0] == vertex]
    
    def edge_exists(
        self,
        v1: str,
        v2: str,
    ) -> bool:
        """
        Determine if an edge exists from v1 to v2.
        """
        return (v1, v2) in self.edges