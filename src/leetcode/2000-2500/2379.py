class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        travellable = (mainTank - 1) // 4
        return (
            10 * (mainTank + travellable)
            if travellable < additionalTank
            else 10 * (mainTank + additionalTank)
        )
