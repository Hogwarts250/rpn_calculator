from tkinter import *
from tkinter import ttk
from rpn_calculator import solve_equation, parse_user_input

# Attempts to pass the given equation into parse_user_input then solve_equation.
def calculate(*args):
    try:
        parsed_input = parse_user_input(equation.get())

    except ValueError:
        parsed_input = ""
    
    if parsed_input:
        try:
            answer.set(solve_equation(parsed_input))
        
        except IndexError:
            pass

root = Tk()
root.title("Reverse Polish Notation Calculator")

equation = StringVar()
answer = StringVar()

# Creates a parent mainframe (grid) that all of the widgets will be children of.
mainframe = ttk.Frame(root, padding = (3, 3, 12, 12))
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))

# Creates an input box for the user to type in their equation.
equation_entry = ttk.Entry(mainframe, width = 20, textvariable = equation)
equation_entry.grid(column = 1, row = 0, sticky = (N, W, E, S))

ttk.Button(mainframe, text = "Enter", command = calculate).grid(column = 1, row = 1, sticky = (N, E, S))
# Automaically updating label that displays the answer.
ttk.Label(mainframe, textvariable = answer).grid(column = 1, row = 2, sticky = (N, E, S))

ttk.Label(mainframe, text = "step 1: input equation").grid(column = 0, row = 0, sticky = (N, W, E, S))
ttk.Label(mainframe, text = "step 2: ???").grid(column = 0, row = 1, sticky = (N, W, S))
ttk.Label(mainframe, text = "step 3: answer").grid(column = 0, row = 2, sticky = (N, W, S))

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
mainframe.columnconfigure(1, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.rowconfigure(1, weight = 1)
mainframe.rowconfigure(2, weight = 1)

# Automatically adds padding to all of the widgets.
for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

equation_entry.focus()
# Binds the "enter" key press to calculate function.
root.bind("<Return>", calculate)

root.mainloop()