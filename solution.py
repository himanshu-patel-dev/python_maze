class Solution:
	# maze: 2D array of characters
	# maze = [
  #   ['S', '0', '1', '0'],
  #   ['1', '0', '1', '0'],
  #   ['1', '0', '0', '0'],
  #   ['1', '1', '0', 'E']
	# ]
	# start_position: (0,0)
	# return: Array of tuples [ (0,1),(1,1) ]
	def get_path(self, maze, start_position):
		if not maze:
			return []
		row, col = len(maze), len(maze[0])
		visited = [[False for _ in range(col)] for _ in range(row)]
		return self.get_path_util(maze, start_position, visited)

	def get_path_util(self, maze, position, visited):
		x,y = position[0], position[1]
		if ( x == len(maze) or y == len(maze[0]) or x < 0 or y < 0 ):
			return []
		if (maze[x][y] == '1' or visited[x][y]):
			return []
		if (maze[x][y] == 'E'):
			return [(x,y)]
		final_path = []
		visited[x][y] = True
		for dx, dy in  [(0,1),(0,-1),(1,0),(-1,0)]:
			path = self.get_path_util(maze, (x+dx, y+dy), visited)
			final_path = path
		visited[x][y] = False
		if final_path:
			return [(x,y)] + final_path
		return final_path
