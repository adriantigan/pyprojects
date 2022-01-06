from sys import argv 



kelvin_temp = ((float(argv[1]))+ 273.15)
print(f"Kelvin temperature is: {kelvin_temp}")


celsius_temperature = ((float(argv[1])) * 9 / 5 + 32)
print(f"Celsius temperature is: {celsius_temperature}")


fahrenheit_temperature = ((float(argv[1])) - 273.15) 
print(f'Fahrenheit temp is: {fahrenheit_temperature}')


