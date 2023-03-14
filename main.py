import sys


class Graph:

    def __init__(self, adjacency: list):
        self.__vertices = len(adjacency)
        Graph.__validate(adjacency)
        self.__adjacency = adjacency

    def floyd(self, view=False) -> list:
        distance = [[self.__adjacency[i][j] if self.__adjacency[i][j] != 0 else sys.maxsize
                     for j in range(self.__vertices)] for i in range(self.__vertices)]
        for i in range(self.__vertices):
            distance[i][i] = 0
        for k in range(self.__vertices):
            for i in range(self.__vertices):
                for j in range(self.__vertices):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        if view:
            self.__print_solution(distance)

        return distance

    @staticmethod
    def __validate(adjacency: list) -> None:
        assert adjacency is not None, 'Adjacency matrix must be not None.'
        assert len(adjacency) == len(adjacency[0]), 'Adjacency matrix must be square.'

    def __print_solution(self, distance: list) -> None:
        for i in range(self.__vertices):
            for j in range(self.__vertices):
                if distance[i][j] == sys.maxsize:
                    print("None", end=" ")
                else:
                    print(distance[i][j], end="  ")
            print(" ")
