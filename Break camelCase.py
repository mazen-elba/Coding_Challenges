# Complete the solution so that the function will break up camel casing, using a space between words.

def solution(str):
	# create variables for new string, lowercase alphabets
	new_str = ''
	lower_alpha = 'abcdefghijklmnopqrstuvwxyz'

	# iterate through string's characters
	for i in str:
		# if current character is lowercase, add character to end of new string
		if i in lower_alpha:
			new_str += i
		# otherwise, current character is uppercase
        # add a space to end of new string, then add uppercase character
		else:
			new_str += ' ' + i 

	return new_str

# --- Test Cases --- #
print(solution("helloWorld")) 		# => "hello World"
print(solution("camelCase")) 		# => "camel Case"
print(solution("breakCamelCase")) 	# => "break Camel Case"