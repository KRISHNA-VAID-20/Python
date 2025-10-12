# import tkinter as tk

# # Create the main application window
# root = tk.Tk()
# root.title("Hello Tkinter")

# # Create a label widget
# label = tk.Label(root, text="Welcome to Tkinter!")
# label.pack()

# # Create a button widget
# button = tk.Button(root, text="Click Me", command=root.destroy)
# button.pack()

# # Run the application
# root.mainloop()

#--------------------------------------------------------------------------------------------------------------

import tkinter as tk
from math import pi

# Function to calculate the area
def calculate_area():
    try:
        radius = float(entry_radius.get())  # Get the radius from the input field
        area = pi * radius**2              # Calculate the area
        label_result.config(text=f"Area: {area:.2f}")  # Display the result
    except ValueError:
        label_result.config(text="Invalid input. Please enter a number.")

# Create the main window
root = tk.Tk()
root.title("Circle Area Calculator")

# Create and place widgets
label_instruction = tk.Label(root, text="Enter the radius of the circle:")
label_instruction.pack(pady=5)

entry_radius = tk.Entry(root)
entry_radius.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate Area", command=calculate_area)
button_calculate.pack(pady=5)

label_result = tk.Label(root, text="Area: ")
label_result.pack(pady=10)

# Run the application
root.mainloop()
