# Choose a text in capital letters including or not digits and non alphabetic characters, and do the following:
# 1. Shift each letter by a given number, but the transformed letter must be a letter (circular shift)
# 2. Replace each digit by its complement to 9
# 3. Keep such as non alphabetic and non digit characters
# 4. Downcase each letter in odd position, upcase each letter in even position (first character is in position 0)
# 5. Reverse the whole result


def pass_play(s, n):

	# Step 1, 2, 3
	new_str = ''
	for char in s:
		if char.isdigit():
			new_str += str(9 - int(char))
		elif char.isalpha():
			shift_str = ord(char.lower()) + n
			new_str += chr(shift_str) if shift_str <= ord('z') else char(shift_str - 26)
		else:
			new_str += char

	# Step 4
	cased_str = ''
	for i in range(len(new_str)):
		cased_str += new_str[i].upper() if i % 2 == 0 else new_str[i].lower()

	# Step 5
	return cased_str[::-1]

# --- Test Cases --- #
print(pass_play('I LOVE YOU!!!', 1)) 	# => !!!vPz fWpM J
print(pass_play('BORN IN 2015!', 1)) 	# => !4897 Oj oSpC
print(pass_play('IS THIS FUNCTION WORKING, AGENT 007?', 3)) 	# => ?299 WqHjD ,jQlNuRz qRlWfQxI VlKw vL