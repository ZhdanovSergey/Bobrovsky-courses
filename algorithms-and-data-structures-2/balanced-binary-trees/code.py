import math

def GenerateBBSTArray(input_arr):
	def addKeyRecursively(start_index, end_index, target_index):
		target_left_index = target_index * 2 + 1
		target_right_index = target_index * 2 + 2

		if start_index == end_index:
			result_arr[target_index] = input_arr[end_index]
		elif start_index + 1 == end_index:
			result_arr[target_index] = input_arr[end_index]
			result_arr[target_left_index] = input_arr[start_index]
		else:
			middle_index = math.ceil((start_index + end_index) / 2)
			result_arr[target_index] = input_arr[middle_index]
			addKeyRecursively(start_index, middle_index - 1, target_left_index)
			addKeyRecursively(middle_index + 1, end_index, target_right_index)

	result_arr = [None] * (2 ** math.ceil(math.log(len(input_arr) + 1, 2)) - 1)

	if len(input_arr) > 0:
		input_arr.sort()
		addKeyRecursively(0, len(input_arr) - 1, 0)

	return result_arr