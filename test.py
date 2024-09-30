from solution import Solution
import inspect

class Test:
	def __init__(self):
		self.sol_obj = Solution()

	def run_all_tests(self):
		# get all methods on instance
		methods = inspect.getmembers(self, predicate=inspect.ismethod)
		# filter out those methods which have 'test_' in them
		test_methods = [method for name, method in methods if name.startswith('test_')]
		# call all othse 'test_' methods
		for i, test in enumerate(test_methods):
				test(i+1)

	def tests_evaluator(
		self,
		test_num,
		maze,
		start_position,
		expected_path
	):
		try:
			actual_path = self.sol_obj.get_path(maze, start_position)
			correct = expected_path == actual_path
		except Exception as e:
			correct = False
			# raise e
		finally:
			output = "\u274c" # red cross
			if correct:	# green tick
				output = "\u2705"
			print(f"Test {test_num} output: {output}")
	
	def test_1(self, test_number):
		maze = [
			['S', '0', '0'],
			['0', '1', '0'],
			['0', '1', 'E'],
		]
		start_position = (0,0)
		expected_path = [
			(0,0),(0,1),(0,2),(1,2),(2,2)
		]
		self.tests_evaluator(test_number, maze, start_position, expected_path)

	def test_2(self, test_number):
		maze = [
			['S', 'E'],
		]
		start_position = (0,0)
		expected_path = [
			(0,0), (0,1)
		]
		self.tests_evaluator(test_number, maze, start_position, expected_path)

	def test_3(self, test_number):
		maze = []
		start_position = (0,0)
		expected_path = []
		self.tests_evaluator(test_number, maze, start_position, expected_path)

	def test_4(self, test_number):
		maze = [
			['S', '0', '0']
		]
		start_position = (0,0)
		expected_path = []
		self.tests_evaluator(test_number, maze, start_position, expected_path)

	def test_5(self, test_number):
		maze = [
			['S', '0', '0', '0'],
			['1', '0', '0', '0'],
			['0', 'E', '0', '0']
		]
		start_position = (0,0)
		expected_path = [
			(0,0), (0,1), (1,1), (2,1)
		]
		self.tests_evaluator(test_number, maze, start_position, expected_path)

	def test_6(self, test_number):
		maze = [
			['E', '0', '0', '0'],
			['1', '1', '1', '0'],
			['S', '0', '0', '0']
		]
		start_position = (2,0)
		expected_path = [
			(2,0), (2,1), (2,2), (2,3), (1,3), (0,3), (0,2), (0,1), (0,0)
		]
		self.tests_evaluator(test_number, maze, start_position, expected_path)

# run all test cases
Test().run_all_tests()
