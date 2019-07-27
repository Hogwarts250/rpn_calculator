import json
from fractions import Fraction

# Attempts to retrieve and return a value from answer.json and None if it can't.
def load_prev_ans():
    with open("answer.json") as f:
        try:
            previous_ans = Fraction(json.load(f))

        except json.decoder.JSONDecodeError:
            previous_ans = None
        
        except TypeError:
            previous_ans = None
    
    return previous_ans

# Overrides all values in answer.json with the input value.
def save_ans(answer):
    with open("answer.json", "w") as f:
        json.dump(answer, f, ensure_ascii=False)

# Clears everything saved in answer.json.
def clear_ans():
    with open("answer.json", "w") as f:
        json.dump(None, f, ensure_ascii=False)