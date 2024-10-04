#class Solution:
	# maze: 2D array of characters
	# maze = [
  #   ['S', '0', '1', '0'],
  #   ['1', '0', '1', '0'],
  #   ['1', '0', '0', '0'],
  #   ['1', '1', '0', 'E']
	# ]
	# return: Array of tuples [ (0,1),(1,1) ]
	#def get_path(self, maze):
		#return [(0,0)]

from collections import deque
class Solution:
    def get_path(self, maze, start_position):
        # Check if the maze is empty
        if not maze or not maze[0]:
            return []

        rows = len(maze)
        cols = len(maze[0])
       
        # Direction vectors for moving in 4 directions (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
       
        # Queue for BFS: stores (current_position, path_taken)
        queue = deque([(start_position, [start_position])])
       
        # Visited set to keep track of visited nodes
        visited = set([start_position])
       
        while queue:
            (current_row, current_col), path = queue.popleft()
           
            # If we've reached the end, return the path
            if maze[current_row][current_col] == 'E':
                return path
           
            # Explore all 4 possible directions
            for dr, dc in directions:
                next_row, next_col = current_row + dr, current_col + dc
               
                # Check if the next cell is within bounds and is not a wall or visited
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if maze[next_row][next_col] != '1' and (next_row, next_col) not in visited:
                        # Mark it as visited and add to queue with the new path
                        visited.add((next_row, next_col))
                        queue.append(((next_row, next_col), path + [(next_row, next_col)]))
       
        # If there's no path, return an empty list
        return []

