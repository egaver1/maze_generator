# maze_generator
Generates a maze with the given minimum path and node count and draws a picture of it.

## Usage
run ``./maze.exe <maze.json or 'r'> <min # lines needed to travel to reach END><max # of nodes>``

- maze.json or any other filename is the name of a maze file to be loaded and drawn alternatively you can enter r for a random maze (use the included maze.json as an example)!
- I think the other arguments are self-explanatory

*I suggest keeping a fair distance between min #lines and max #nodes (with #nodes always greater than #lines) to keep performance high*

## How it can help you for the project
This maze is pretty similar to how your phone lines should be, with the nodes representing switch boards where numbers reside. 
If you can figure out how to write a ``navigate`` function which takes the maze as a dictionary and produces the minimum distance needed to
reach the end starting at node '0' then this could help you practice (also hopefully the visual just helps).

## Using the source code
To use the source code you will first need to install the relevant packages by using:
``pip install -r requirements.txt``
Next, just place ``import maze`` at the top of your file and you can now use the ``mazeTesting`` object!. To access the maze dictionary just use
```
maze = maze.mazeTesting(None, 2, 10)
myMaze = maze.maze
```
the None argument just lets it know you want a random maze instead of one loaded from a file!

Hope this helps and sorry for the bugs in advance!
