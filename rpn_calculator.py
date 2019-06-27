import operator

# Converts an input string into a list of stings by seperating at the spaces and tries to literally evaluate each string.
def parse_user_input(user_input):
    list_input_char = user_input.split(" ")

    for index, char in enumerate(list_input_char):
        try:
            list_input_char[index] = (eval(char))
        except SyntaxError:
            pass
    
    return list_input_char

# Takes an input of 3 characters and tries to solve it using RPN. Returns the answer if it suceedes and returns None it if doesn't.
def solve_three_chars(char1, char2, char3):
    ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv, '//' : operator.floordiv,
        '%' : operator.mod, '**' : operator.pow}

    if (type(char1) is int or float) and (type(char2) is int or float) and (char3 in ops):
        output = ops[char3](char1, char2)

    try:
        return(output)
    except UnboundLocalError:
        return None

# Loops through an input list and solves it using RPN. 
def solve_equation(list_char_eval):
    for index in range(len(list_char_eval)):
        if len(list_char_eval) == 1:
            break

        solve_output = solve_three_chars(list_char_eval[index], list_char_eval[index + 1], list_char_eval[index + 2])
        if solve_output != None:
            # Deletes the first two characters, converts the third into the answer from solve_three_chars, and recurs itself.
            del list_char_eval[index : index + 2]
            list_char_eval[index] = solve_output

            solve_equation(list_char_eval)
    
    return(list_char_eval[0])

while True:
    user_input = input("Input your equation in reverse polish notation: ")
    print(solve_equation(parse_user_input(user_input)))

    if input("Do you have another equation to solve? (y/n)? ") == "n":
        break