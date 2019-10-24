from enum import Enum

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Directions(Enum):
    Up = 0
    Right = 1
    Left = 2
    Down = 3


class Solution:
    def move(self, cell, direction):
        if direction == Directions.Up:
            return (cell[0] - 1, cell[1])
        if direction == Directions.Right:
            return (cell[0], cell[1] + 1)
        if direction == Directions.Down:
            return (cell[0]+1, cell[1])
        if direction == Directions.Left:
            return (cell[0], cell[1] - 1)

    def go_back(self):
        self.robot.turnRight()
        self.robot.turnRight()
        self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()

    def backtrack(self, cell=(0, 0), direction=Directions.Up):
        self.visited.add(cell)
        self.robot.clean()
        for direction in Directions:
            new_cell = self.move(cell, direction)
            if not new_cell in self.visited and self.robot.move():
                self.backtrack(new_cell, direction)
                self.go_back()
            self.robot.turnRight()

    def cleanRoom(self, robot):
        """ This function is only the one called from outside
        :type robot: Robot
        :rtype: None
        """

        self.visited = set()
        self.robot = robot
