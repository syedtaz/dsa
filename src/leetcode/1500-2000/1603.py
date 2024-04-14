class ParkingSystem:
    state: list[int]
    occupancy: tuple[int, int, int]

    def __init__(self, big: int, medium: int, small: int) -> None:
      self.occupancy = (big, medium, small)
      self.state = [0, 0, 0]

    def addCar(self, carType: int) -> bool:
      if self.state[carType - 1] == self.occupancy[carType - 1]:
         return False

      self.state[carType - 1] += 1
      return True