# Split the string into pairs of two characters. 
# If the string contains an odd number of characters, replace missing second character of final pair with an underscore ('_')

def solution(string):
	# add '_' to end of string if odd number of elements
	if len(string) % 2:
		string += '_'

	pairs = []

	# iterate thru string's elements; increment by 2
	idx = 0
	while idx < len(string) - 1:
		# concatenate current and next elements
		pairs.append(string[idx] + string[idx+1])
		idx += 2

	return pairs




# --- Test Cases --- #
print(solution("asdfadsf"))	 # => ['as', 'df', 'ad', 'sf']
print(solution("asdfads"))	 # => ['as', 'df', 'ad', 's_']
print(solution(""))	 		 # => []
print(solution("x"))	 	 # => ["x_"]