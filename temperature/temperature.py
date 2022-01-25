from sys import argv 

"""
Extinde functionalitatea programului asa incat
sa nu mai presupunem ca numaru ce il dai ii in
grade Celsius, ci tu sa specifici in ce grade e
--------------------------------------------------------
Implementarea curenta:
python temperature.py 23 kelvin

23 - presupunem ca is 23 grade celsius
kelvin - in ce grade convertim 23(celsius to kelvin)
--------------------------------------------------------
Implementare noua:
python temperature.py 23 celsius kelvin

23 - un numar oarecare
celsius - presupunem ca numarul oarecare e in celsius
kelvin - gradele in care sa fie transformate cele 23 grade celsius

Exemple:
python temperature.py 2312 kelvin celsius
    2312 grade kelvin in celsius
python temperature.py 32 fahrenheit kelvin
    2312 grade fahrenheit in kelvin
python temperature.py 77 kelvin fahrenheit
    77 grade kelvin in fahrenheit
etc.

Acuma ca stii sa folosesti functii, creeaza noi
functii sau extinde-le pe cele actuale asa incat
sa calculeze toate combinatiile:
    kelvin_to_celsius
    fahrenheit_to_kelvin
    celsius_to_fahrenheit
    etc.

La verificarea cu ifurile si elifurile trebuie sa
verifici ambele argumente(ambele cuvinte date la terminal)
asa incat sa stii ce functie sa apelezi 
"""

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