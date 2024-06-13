#isalnum() Returns True if all characters in the string are alphanumeric(Letters and Numbers)
#Should come up and say True/False

word_four='sdfsfdf'
#test_user_input_for_alphanumeric=word_four.isalnum
print(word_four.isalnum)

'''
Take time to figure out isdecimal(), isnumeric(), isalpha(), etc.
'''

num_one='12345' #True
num_two='4.123' #false
num_three='abcde' #False

print(num_one.isdecimal())
print(num_two.isdecimal())

#isdigit returns true if all characters int he string are digits
print(num_one.isdigit()) 

#WHY IS EVERYTHING SHOW UP INVALID SYNTAX?????

#superscripts are not decimal
