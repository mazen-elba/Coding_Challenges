# Function takes as argument a sequence and returns a list of items without any elements with the same value next to each other
#... and preserves the original order of elements.

def unique_in_order(iterable):
	duplicates = []

	# iterate through sequence's items
	for item in iterable:
		# add current item to new sequence if
		# ... number of items in new sequence < 1
		# ... or, current item does not match the last item in new sequence
		if (len(duplicates) < 1) or (item != duplicates[len(duplicates) - 1]):
			duplicates.append(item)

	return duplicates

# --- Test Cases --- #
print(unique_in_order('AAAABBBCCDAABBB')) 	# => ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD')) 			# => ['A', 'B', 'C', 'c', 'A', 'D']
print(unique_in_order([1,2,2,3,3])) 		# => [1,2,3]
print(unique_in_order([16,16,83,40,40,83])) # => [16,83,40,83]