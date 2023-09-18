# Import the sleep function from the time module, so
# that the sleep function can be used in this program.
from time import sleep

# Prompt the user to enter her name.
name = input("Hello! What is your name? ")

# Print the numbers 3, 2, 1.
for i in range(3, 0, -1):
    print(i, flush=True)
    sleep(0.5)  # Pause for 1/2 second

# Use a Python f-string to format a greeting
# for the user and then print the greeting.
print(f"Welcome to CSE 111, {name}!")



# esto es un comentario 
# estoy seguro que esto tambien es un comentario

length = 5
time = 7.2
in_flight = True
first_name = "cho"

saludos = "hello"
texto = "23"

found = True

x=14
sample = 4.5

color = ["amarillo", "rojo", "green", "blue"]
sampla = [2,54,65,1,6,23,3,5]

students = {
    "42-039-4736": "Clint Huish",
    "61-315-0160": "Amelia Davis",
    "10-450-1203": "Ana Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Amelia Davis"
}

text = input("Please enter your name: ")
color = input("What is your favorite color? ")
