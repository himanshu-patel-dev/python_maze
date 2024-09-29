# python_maze
Maze Runner....;)

Problem:

You are given a 2D array like below

```python
maze = [
    ['S', '0', '1', '0'],
    ['1', '0', '1', '0'],
    ['1', '0', '0', '0'],
    ['1', '1', '0', 'E']
]
```
- "S" is the starting point.
- "E" is the ending point.
- "1" represents a wall.
- "0" represents an open space you can move through.

Task:
You need to write a function that finds the shortest path from the start (S) to the end (E).
And take care of edge cases

Output:
```python
output = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3)]
```

Test:
You can add more test case in `test.py` file to test your code.
```bash
$ python3 test.py 
Test 1 output: ❌
```
