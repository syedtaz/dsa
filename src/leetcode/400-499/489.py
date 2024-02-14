# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
    def move(self) -> bool:
        return True

    def turnLeft(self) -> None:
        return None

    def turnRight(self) -> None:
        return None

    def clean(self):
        return None


class Solution:
    def cleanRoom(self, robot: Robot) -> None:

        seen: set[tuple[int, int]] = set()
        moves = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

        def ninety() -> None:
            robot.turnRight()
            robot.turnRight()

        def traverse(i: int, j: int, dir: int) -> None:
            robot.clean()
            seen.add((i, j))

            for d in range(4):
                nd = (dir + d) % 4
                del_i, del_j = moves[nd]
                ni, nj = i + del_i, j + del_j
                if (ni, nj) not in seen and robot.move():
                    traverse(ni, nj, nd)

                    ninety()
                    robot.move()
                    ninety()

                robot.turnRight()

        traverse(0, 0, 0)
