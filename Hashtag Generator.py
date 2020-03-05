# Let's help them with our own Hashtag Generator!
# Here's the deal:
# ... It must start with a hashtag (#).
# ... All words must have their first letter capitalized.
# ... If the final result is longer than 140 chars it must return false.
# ... If the input or the result is an empty string it must return false.

def generate_hashtag(str):
    # return False if string's length > 140 characters, or an empty string
    if len(str) > 140 or len(str) == 0:
        return False
        
    # capitalize first letter
    if str[0] != '#' and str[0] == str.islower():
        str[0].upper()
        
    # remove all spaces
    spaces = ' '
    new_str = ''
    for i in (0, len(str)-1):
        if str[i:-1] == '#':
            new_str = '#Codewars'

# --- Test Cases --- #
Test.describe("Basic tests")
Test.assert_equals(generate_hashtag(''), False, 'Expected an empty string to return False')
Test.assert_equals(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
Test.assert_equals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
Test.assert_equals(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
Test.assert_equals(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
Test.assert_equals(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
Test.assert_equals(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
Test.assert_equals(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
Test.assert_equals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
Test.assert_equals(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')