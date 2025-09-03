import tkinter as tk
from tkinter import messagebox
from quinary import Calc  

calculator = Calc()


root = tk.Tk()
root.title("Quinary Calculator")

#Display
display = tk.Entry(root, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=4)


#This shows if toggle on or off, as well showing the lastest number 
def refresh_display():
    if show_decimal.get():
        text = calculator.get_display_decimal()    
    else:
        text = calculator.get_display_quinary()   
    display.delete(0, tk.END)
    display.insert(0, text)

# Deals with displaying the numebr 
def press_digit(digit):
    try:
        calculator.push_digit(digit)
        refresh_display()
    except Exception as error:
        show_error(error)

# This handles when the +, - button is pressed 
def press_operation(operation):
    try:
        calculator.set_operation(operation)
        refresh_display()
    except Exception as error:
        show_error(error)


# works with the equal sign to calculate 
def press_equal():
    try:
        calculator.equal()
        refresh_display()
    except Exception as error:
        show_error(error)

#When C is pressed to clear everything  
def press_clear():
    calculator.clear()
    refresh_display()

#shows error if soemhting went wrong 
def show_error(error):
    display.delete(0, tk.END)
    display.insert(0, "ERROR")
    root.bell()
    messagebox.showerror("Error", str(error))

# TOGGLE
show_decimal = tk.BooleanVar(value=False)
toggle = tk.Checkbutton(root, text="Show Decimal", variable=show_decimal, command=refresh_display)
toggle.grid(row=1, column=0, columnspan=4)

# Showing (0–4) 
tk.Button(root, text="1", width=5, height=2, command=lambda: press_digit("1")).grid(row=2, column=0)
tk.Button(root, text="2", width=5, height=2, command=lambda: press_digit("2")).grid(row=2, column=1)
tk.Button(root, text="3", width=5, height=2, command=lambda: press_digit("3")).grid(row=2, column=2)
tk.Button(root, text="4", width=5, height=2, command=lambda: press_digit("4")).grid(row=3, column=0)
tk.Button(root, text="0", width=5, height=2, command=lambda: press_digit("0")).grid(row=3, column=1)

# Operation buttons 
tk.Button(root, text="+", width=5, height=2, command=lambda: press_operation("+")).grid(row=2, column=3)
tk.Button(root, text="-", width=5, height=2, command=lambda: press_operation("-")).grid(row=3, column=3)
tk.Button(root, text="*", width=5, height=2, command=lambda: press_operation("*")).grid(row=4, column=3)
tk.Button(root, text="/", width=5, height=2, command=lambda: press_operation("/")).grid(row=5, column=3)

# For square root 
tk.Button(root, text="x^2", width=5, height=2, command=lambda: press_operation("sq")).grid(row=4, column=0)
tk.Button(root, text="√",  width=5, height=2, command=lambda: press_operation("sqrt")).grid(row=4, column=1)

# for equal and clear
tk.Button(root, text="=", width=5, height=2, command=press_equal).grid(row=5, column=2)
tk.Button(root, text="C", width=5, height=2, command=press_clear).grid(row=5, column=0)


refresh_display()
root.mainloop()