from json import load, dump
from random import randint, choice, seed
from sys import argv, exit
from networkx import DiGraph, draw
from matplotlib.pyplot import show
from time import time


class mazeTesting:
    def __init__(self, maze=None, minLen=2, numNodes=10):
        if not maze:
            self.maze = dict()
            self.possible = False
            start = time()
            tries = 0
            while not self.possible:
                tries += 1
                print("Attempting", tries)
                self.maze = dict()
                seed(time())
                self.maze_generator('0', self.maze, minLen, [str(i) for i in range(numNodes)])
                end = time()
                if end - start > 60:
                    print("Timed out! Sorry! Please try again with more nodes!")
                    exit(1)

        else:
            if type(maze) != str:
                raise TypeError
            with open(maze, 'r')as file:
                self.maze = load(file)

    def drawMaze(self):
        grap = DiGraph()
        edges = []

        for node in self.maze:
            for y in self.maze[node]:
                if y != "NOPATH":
                    edges.append((node, y))

        grap.add_edges_from(edges)
        draw(grap, with_labels=True, node_size=2000, font_size=10, arrows=True)
        show()

    def maze_generator(self, startPt, maze, minLen, nodes):
        length = randint(0, 5)
        if startPt == "0" and not length:
            length = 1

        if startPt not in maze:
            maze[startPt] = []

            if not length or minLen <= -3:
                maze[startPt] = []
            else:
                for i in range(length):
                    new = choice(nodes)
                    while new == startPt:
                        new = choice(nodes)
                    if new not in maze[startPt]:
                        maze[startPt].append(new)

        if minLen == 1:
            self.possible = True
            maze[startPt].append("END")

        for y in maze[startPt]:
            if y != "END" and (y not in maze):
                self.maze_generator(y, maze, minLen - 1, nodes)

    def saveMaze(self):
        with open("maze.json", 'w')as file:
            dump(self.maze, file, indent=4)


if len(argv) < 3:
    print("Incorrect usage: try ./maze <file_name.json or \'r\' to randomly generate> <min distance to escape the maze 0 if loading from file><number of nodes 0 if using file>")
    exit(1)

maze = None if argv[1] == 'r' else argv[1]
m = mazeTesting(maze, int(argv[2]), int(argv[3]))
m.drawMaze()
option = input("Save maze to maze.json?(y/n): ")
if option.strip().lower() == 'y':
    m.saveMaze()
else:
    exit(0)