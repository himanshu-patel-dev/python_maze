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
		r = self.get_path_util(maze, start_position)
		print(r, start_position)
		return r

	def get_path_util(self, maze, position):
		x,y = position[0], position[1]
		out_of_boundary = ( x >= len(maze) or y >= len(maze[1]) )
		if out_of_boundary:
			return []
		hitting_wall = (maze[x][y] == '1')
		if hitting_wall:
			return [] 
		reached_end = (maze[x][y] == 'E')
		if reached_end:
			return [(x,y)]
		final_path = []
		for dx, dy in  [(0,1),(0,-1),(1,0),(-1,0)]:
			path = self.get_path_util(maze, (x+dx, y+dy))
			if len(final_path) == 0 or len(path) < len(final_path):
				final_path = path
		return final_path
