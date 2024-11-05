import customtkinter as ctk
from tkinter import messagebox

#Initialize the main window with a set geometry and title
window = ctk.CTk()
window.geometry('300x150')
window.title("Temperature Converter")

def validate_input(entry_text):
    """
    Validates the entry box input to allow only numbers and decimal points.
    Returns True if valid, False otherwise.
    """
    # Allow empty input or single decimal point
    if entry_text == "" or entry_text == ".":
        return True
    # Check if input can be converted to a float (valid number)
    try:
        float(entry_text)
        return True
    except ValueError:
        return False

def calc_cels():
    """Calculates Fahrenheit and Kelvin from a Celsius input."""
    # Convert Celsius to Fahrenheit
    x = float(input.get()) * (9/5) + 32
    # Convert Celsius to Kelvin
    y = float(input.get()) + 273.15

    # Display results in labels with two decimal places
    result1.configure(text=f"Temperature in Fahrenheit is {round(x, 2)}°F")
    result2.configure(text=f"Temperature in Kelvin is {round(y, 2)}K")

def calc_fahr():
    """Calculates Celsius and Kelvin from a Fahrenheit input."""
    # Convert Fahrenheit to Celsius
    x = (float(input.get()) - 32) * 5/9
    # Convert Fahrenheit to Kelvin
    y = (float(input.get()) - 32) * 5/9 + 273.15

    # Display results in labels with two decimal places
    result1.configure(text=f"Temperature in Celsius is {round(x, 2)}°C")
    result2.configure(text=f"Temperature in Kelvin is {round(y, 2)}K")

def calc_kelv():
    """Calculates Celsius and Fahrenheit from a Kelvin input."""
    # Convert Kelvin to Celsius
    x = float(input.get()) - 273.15
    # Convert Kelvin to Fahrenheit
    y = (float(input.get()) - 273.15) * 9/5 + 32

    # Display results in labels with two decimal places
    result1.configure(text=f"Temperature in Celsius is {round(x, 2)}°C")
    result2.configure(text=f"Temperature in Fahrenheit is {round(y, 2)}°F")

def conv():
    """
    Determines which unit is selected and calls the appropriate conversion function.
    Check if the value is blank
    """
    try:
        match choices.get():
            case "Celsius":
                calc_cels()
            case "Fahrenheit":
                calc_fahr()
            case "Kelvin":
                calc_kelv()
            case _:
                # Display a warning if no valid unit is selected
                messagebox.showwarning(title="Warning", message="Please choose a valid unit!")
    except ValueError:
        messagebox.showwarning(title="Warning", message="Please enter a valid value!")

# Instruction label
instruction_label = ctk.CTkLabel(window, text="Choose one of the units to convert to the other two:")
instruction_label.place(x=1, y=0)

# Entry box for temperature input
input = ctk.CTkEntry(window)
input.place(x=1, y=30)

# Register the input validation function
vcmd = (window.register(validate_input), "%P")
input.configure(validate="key", validatecommand=vcmd)

# Combobox to select temperature unit
choices = ctk.CTkComboBox(window, values=["Celsius", "Fahrenheit", "Kelvin"], state='readonly')
choices.place(x=150, y=30)

# Submit button to initiate conversion
submit = ctk.CTkButton(window, text="Submit", command=conv)
submit.place(x=1, y=60)

# Labels to display the conversion results
result1 = ctk.CTkLabel(window, text="")
result1.place(x=5, y=90)

result2 = ctk.CTkLabel(window, text="")
result2.place(x=5, y=120)

# Run the main event loop
window.mainloop()