from tkinter import *
from tkinter import ttk
from rpn_calculator import solve_equation, parse_user_input

# Attempts to imput the equation given into parse_user_input then solve_equation.
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

# Creates the parent mainframe (grid) that the widgets will be children of.
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

equation = StringVar()
answer = StringVar()

# Creates an input box for the user to type in their equation.
equation_entry = ttk.Entry(mainframe, width = 20, textvariable = equation)
equation_entry.grid(column = 2, row = 1, sticky = (W, E))

ttk.Button(mainframe, text = "Enter", command = calculate).grid(column = 2, row = 2, sticky = E)
# Automaically updating label displaying the answer
ttk.Label(mainframe, textvariable = answer).grid(column = 2, row = 3, sticky = (W, E))

ttk.Label(mainframe, text="step 1: input equation").grid(column = 1, row = 1, sticky = W)
ttk.Label(mainframe, text="step 2: ???").grid(column = 1, row = 2, sticky = W)
ttk.Label(mainframe, text="step 3: answer").grid(column = 1, row = 3, sticky = W)

# Automatically adds padding to all the children of the mainframe
for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

equation_entry.focus()
# Binds the "enter" key press to calculate function.
root.bind("<Return>", calculate)

root.mainloop()