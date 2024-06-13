print("What is your name?")
first_name=input()
print(f'You typed in {first_name}.')

#Let's shorten our code
first_name=input('What is your name? ')
print(f'You typed in {first_name}.')

print(f'Hello, {first_name}.')
print('Hello', first_name)

#Let's sanitize our string!
length_of_name=len(first_name)
print(f'Hello', {first_name}. I am counting {length_of_name} characters.')
    #There's definitely a syntax error h ere because it's not coloring correctly for length_of_name.
    #It's not surprising this is coming up with "SyntaxError: unterminated string literal (detected at line 14)"

'''
Write some code that will take a string from the user and print if it is a number or not. 
Examples: 
apple
False

4
True
'''

test_one=apple
print(test_one.isnum) #This isn't it, and parenting while taking this class is nearly impossible

user_input=input('What is your magic word?')
#Control+c kills your terminal, but I have no idea what this means or how it's working.