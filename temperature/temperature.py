from sys import argv 


def kelvin(celsius_grades):
    return float(celsius_grades) + 273.15

def fahrenheit(celsius_grades):
    return float(celsius_grades) * 9 / 5 - 32


if argv[2] == "kelvin": 
    print(f"Kelvin temperature is: {kelvin(argv[1])}")

elif argv[2] == "celsius": 
    print(f"Celsius temperature is: {argv[1]}")  

elif argv[2] == "fahrenheit":   
    print(f'Fahrenheit temperature is: {fahrenheit(argv[1])}')