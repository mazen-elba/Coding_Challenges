# A stream of data is received and needs to be reversed.
# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:
# ... 11111111 (byte1)  00000000 (byte2)  00001111 (byte3)  10101010 (byte4)
# should become:
# ... 10101010 (byte4)  00001111 (byte3)  00000000 (byte2) 11111111 (byte1)
# The total number of bits will always be a multiple of 8.

def data_reverse(data):
	byte_seq = []
	idx = 0
	while idx in range(len(data)-1):
		byte_seq.append(data[idx:idx+8])
		idx += 8 	# increment by 8-bits

	reversed_data = []
	# iterate thry byte_seq's 2D matrix
	for row in byte_seq:
		# iterate thru each row's first 8 elements backwards
		for ele in row[:8][::-1]:
			# add current element to new array
			reversed_data.append(ele)

	# return reversed data array in descending order
	return reversed_data[::-1]

# --- Test Cases --- #
data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
print(data_reverse(data1)) # => [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

data2 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
print(data_reverse(data2)) # => [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]

data3 = [0,0,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,1]
print(data_reverse(data3)) # => [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0]