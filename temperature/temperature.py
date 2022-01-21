from sys import argv 

#if argv[2] == "celsius":
    #celsius_temperature = (float(argv[1])) * 9 / 5 + 32
    #print(f"Celsius temperature is: {celsius_temperature}")


if argv[2] == "kelvin":
    kelvin_temp = (float(argv[1]))+ 273.15
    print(f"Kelvin temper;ature is: {kelvin_temp}")
elif argv[2] == "celsius": 
    celsius_temperature = (float(argv[1]))+ 273.15
    print(f"kelvin is: {celsius_temperature}")
    
if argv[2] == "fahrenheit":
    fahrenheit_temperature = (float(argv[1])) * 9 / 5 - 32
    print(f'Fahrenheit temperature is: {fahrenheit_temperature}')

elif argv[2] == "celsius": 
    celsius_temperature = (float(argv[1]) * 9 / 5+ 32 )
    print(f"fahrenheit is  {celsius_temperature}")