# Complete the solution so that the function will break up camel casing, using a space between words.

def solution(str):
	new_str = ''
	lower_alpha = 'abcdefghijklmnopqrstuvwxyz'

	for i in str:
		if i in lower_alpha:
			new_str += i
		else:
			new_str += ' ' + i 

	return new_str

# --- Test Cases --- #
print(solution("helloWorld")) 		# => "hello World"
print(solution("camelCase")) 		# => "camel Case"
print(solution("breakCamelCase")) 	# => "break Camel Case"