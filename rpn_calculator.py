import operator, json
from fractions import Fraction
from json_interaction import load_prev_ans, save_ans, clear_ans

# Converts an input string into a list of strings by seperating at the spaces and tries to literally evaluate each string.
def parse_user_input(user_input):
    list_input_char = user_input.split(" ")

    for char in list_input_char:
        if not char.strip():
            list_input_char.remove(char)

    # Replaces all numeric strings with floats / ints, fractions if possible, and "ans" with the stored ans
    for index, value in enumerate(list_input_char):
        if value in {"+", "-", "*", "/", "%", "**", "//"}:
            pass

        elif value == "ans":
            list_input_char[index] = load_prev_ans()

        elif value == "clear":
            clear_ans()

        else:
            list_input_char[index] = Fraction(value)

    list_input_char = [x for x in list_input_char if x != "clear"]

    return list_input_char

# Takes an input of 3 characters and tries to solve it. Returns the answer if it suceedes and returns None it if doesn't.
def solve_three_chars(char1, char2, char3):
    ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv, '%' : operator.mod, '**' : operator.pow}
    
    if (type(char1) is int or float) and (type(char2) is int or float) and (char3 in ops):
        if char3 == "//":
            char2 = Fraction(1 / char2)
            char3 = "**"
        
        output = ops[char3](char1, char2)
        return output

    else:
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
    
    # Automatically saves answer in .json file
    save_ans(str(list_char_eval[0]))

    return(list_char_eval[0])

while True:
    user_input = input("\n")

    if user_input == "exit":
        break
    
    parsed_input = parse_user_input(user_input)
    
    if len(parsed_input) == 0:
        pass
        
    else:
        print(str(solve_equation(parsed_input)))