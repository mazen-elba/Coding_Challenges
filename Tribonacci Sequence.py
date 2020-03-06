# Works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next.
# need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.
# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array.

def tribonacci(signature, n):
	trib_seq = []

	for i in range(n):
		# sum up the last 3 numbers of current sequence/queue to make newest element
		new_number = signature[-1] + signature[-2] + signature[-3]
		# add the newest element to the end of the current sequence/queue
		signature.append(new_number)
		# remove and assign top element from queue to a new variable
		current_number = signature.pop(0)
		# add the new variable (newest element)
		trib_seq.append(current_number)

	return trib_seq	

# --- Test Cases --- #
print(tribonacci([1, 1, 1], 10)) 		# => [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([0, 0, 1], 10)) 		# => [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
print(tribonacci([0, 1, 1], 10)) 		# => [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
print(tribonacci([1, 0, 0], 10)) 		# => [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
print(tribonacci([0, 0, 0], 10)) 		# => [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(tribonacci([1, 2, 3], 10)) 		# => [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
print(tribonacci([3, 2, 1], 10)) 		# => [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
print(tribonacci([1, 1, 1], 1))  		# => [1]
print(tribonacci([300, 200, 100], 0)) 	# => []
print(tribonacci([0.5, 0.5, 0.5], 30)) 	# => [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5]