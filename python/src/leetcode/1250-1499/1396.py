class UndergroundSystem:
    state: dict[tuple[str, str], tuple[int, int]]
    transit: dict[int, tuple[str, int]]

    def __init__(self) -> None:
        self.state = {}
        self.transit = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.transit[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        source, start = self.transit.pop(id)
        key = (source, stationName)
        if key not in self.state:
            self.state[key] = (t - start, 1)
        else:
            total, count = self.state[key]
            self.state[key] = (total + (t - start), count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        if key not in self.state:
            return 0.0
        total, count = self.state[key]
        return total / count
