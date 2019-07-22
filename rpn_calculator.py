import operator, math
from fractions import Fraction
from json_interaction import load_prev_ans, save_ans, clear_ans

# Converts an input string into a list of strings by seperating at the spaces and tries to literally evaluate each string.
def parse_user_input(user_input):
    list_input_char = user_input.split(" ")
    output_list = []

    inverse_trig_relations = {"sin-1" : "asin", "cos-1" : "acos", "tan-1" : "atan"}

    for char in list_input_char:
        if not char.strip():
            list_input_char.remove(char)

    # Replaces all numeric strings with floats / ints, fractions if possible, and "ans" with the stored ans.
    for value in list_input_char:
        if value in ["+", "-", "*", "/", "%", "**", "//"]:
            output_list.append(value)

        # Puts a 1 in front of trig functions to avoid conflictions with solve_three_chars.
        elif value in ["sin", "cos", "tan", "sin-1", "cos-1", "tan-1"]:
            if value in inverse_trig_relations:
                output_list.extend([-1, inverse_trig_relations[value]])
            
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

# Takes an input of 3 characters and tries to solve it. Returns the answer if it suceedes and returns None it if doesn't.
def solve_three_chars(char1, char2, char3):
    ops = {"+" : operator.add, "-" : operator.sub, "*" : operator.mul, "/" : operator.truediv, "%" : operator.mod, "**" : operator.pow, "//": None} 
        
    special_ops = {"sin" : math.sin, "cos" : math.cos, "tan" : math.tan, "asin" : math.asin, "acos" : math.acos, "atan" : math.atan}
    
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

            if char3 == "asin" or "acos" or "atan":
                return math.degrees(output)
                
            else:
                return output

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
    
    # Automatically saves answer in .json file.
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