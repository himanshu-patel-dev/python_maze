from solution import Solution

class Test:
	def __init__(self):
		self.sol_obj = Solution()

	def main(self):
		self.test1()

	def test_runner(
		self,
		test_num,
		maze,
		expected_path
	):
		actual_path = self.sol_obj.get_path(maze)
		correct = expected_path == actual_path
		if correct:	# if true then check
			output = "\u2705"
		else:			# else false
			output = "\u274c"
		print(
			f"Test {test_num} output: {output}"
		)

	def test1(self):
		maze = [
			['S', '0', '0'],
			['0', '1', '0'],
			['0', '1', 'E'],
		]
		expected_path = [
			(0,0),(0,1),(0,2),(1,2),(2,2)
		]
		self.test_runner(
			1, maze, expected_path
		)

# run all test cases
Test().main()
