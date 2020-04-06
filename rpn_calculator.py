import operator, math
from fractions import Fraction
from json_interaction import load_prev_ans, save_ans, clear_ans

# Converts an input string into a list of strings and then evaluates each value.
def parse_user_input(user_input):
    list_input_char = user_input.split(" ")
    output_list = []

    inverse_trig_funcs = ["sin-1", "cos-1", "tan-1"]

    # Checks if a value is empty and removes it if it is.
    for char in list_input_char:
        if not char.strip():
            list_input_char.remove(char)

    # Replaces all numeric strings with fractions, "ans" with the stored ans, and modifies trig functions.
    for value in list_input_char:
        if value in ["+", "-", "*", "/", "%", "**", "//"]:
            output_list.append(value)

        elif value in ["sin", "cos", "tan", "sin-1", "cos-1", "tan-1"]:
        # Puts a placeholder 1 in front of trig functions in order to avoid problems with solve_three_chars.
            if value in inverse_trig_funcs:
                output_list.extend([-1, value])
            
            else:
                output_list[-1] = math.radians(output_list[-1])
                output_list.extend([1, value])

        elif value == "ans":
            output_list.append(load_prev_ans())

        elif value == "clear":
            clear_ans()

        else:
            output_list.append(Fraction(value))

    return output_list

# Takes an input of 3 characters and attempts to solve it.
def solve_three_chars(char1, char2, char3):
    ops = {"+" : operator.add, "-" : operator.sub, "*" : operator.mul, "/" : operator.truediv, 
        "%" : operator.mod, "**" : operator.pow, "//": None} 
    special_ops = {"sin" : math.sin, "cos" : math.cos, "tan" : math.tan, "sin-1" : math.asin, 
        "cos-1" : math.acos, "tan-1" : math.atan}
    inverse_trig_funcs = ["sin-1", "cos-1", "tan-1"]

    if (type(char1) is int or float) and (type(char2) is int or float):
        # Handles basic mathematical equations.
        if char3 in ops:
            if char3 == "//":
                char2 = Fraction(1 / char2)
                char3 = "**"
            
            output = ops[char3](char1, char2)
            return output

        # Handles trignometric equations.
        elif char3 in special_ops:
            output = special_ops[char3](char1)
            
            if char3 in inverse_trig_funcs:
                return math.degrees(output)
                
            else:
                return output

    return None

# Loops through an input list and solves it using RPN. 
def solve_equation(list_char_eval):
    for index in range(len(list_char_eval)):
        if len(list_char_eval) == 1:
            # Automatically saves answer in .json file.
            save_ans(str(list_char_eval[0]))
            return(list_char_eval[0])

        solve_output = solve_three_chars(list_char_eval[index], list_char_eval[index + 1], list_char_eval[index + 2])
        
        if solve_output != None:
            # Deletes the first two values, sets the third equal to the answer from solve_three_chars.
            del list_char_eval[index : index + 2]
            list_char_eval[index] = solve_output

            solve_equation(list_char_eval)
    
"""
while True:
    user_input = input("\n")

    if user_input == "exit":
        break
    
    parsed_input = parse_user_input(user_input)
    
    if len(parsed_input) == 0:
        pass
        
    else:
        print(str(solve_equation(parsed_input)))
"""