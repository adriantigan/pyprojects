from sys import argv


def temperature(c_to_f):
    return float(c_to_f) * 9 / 5 + 32
    


def fahrenheit_to_celsius(temp):
     return float(temp) * 9 / 5 - 32


def celsius_to_kelvin(temp):
    return float(temp)  + 237.15

def kelvin_to_celsius(temp):
      return float(temp) - 273.15
    


def fahrenheit_to_kelvin(temp):
    return 5 / 9 * (float(temp) - 32 ) + 273.15


def kelvin_to_fahrenheit(temp):
    return 1.8 * (float(temp)- 273.15)  + 32 




# def kelvin(celsius_grades):
#     return float(celsius_grades) - 273.15


# def fahrenheit(celsius_grades):
#     return float(celsius_grades) * 9 / 5 - 32




    
# if argv[2] == "kelvin": 
#     print(f"Kelvin temperature is: {kelvin(argv[1])}")

#     print(f"celsius temperature is: ")
# if argv[2] == "celsius": 
#     print(f"Celsius temperature is: {argv[1]}")  

# elif argv[2] == "fahrenheit":   
#     print(f'Fahrenheit temperature is: {fahrenheit(argv[1])}')