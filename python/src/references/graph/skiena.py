from dataclasses import dataclass


@dataclass
class Graph:
    nodes: dict[int, list[int]]


# 7.5 Linear time algorithm to find chromatic number of a graph with
# degree at most 2.


def chrom(x: Graph) -> int:
    edges = [y for e in x.nodes.values() for y in e]
    match len(edges):
        case 0:
            return 0
        case 1:
            return 2
        case _:
            seen: set[int] = set()
            for e in edges:
                if e in seen:
                    return 3
                seen.add(e)
            return 2
