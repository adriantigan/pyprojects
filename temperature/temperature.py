from sys import argv

temp_cel = (float(argv[1]))

fahren_temp = (float(argv[1]) * 1.8) + 32

new_temp = (float(argv[1]) * 0.33000 )


kev_temp = (float(argv[1])) + 273.15

print(f"Kelvin temperature is: {kev_temp}")
print(f"fahrenheit temperature is: {fahren_temp}")
print(f"newton temperature is:{new_temp}")
print(f"Celsius temperature is: {temp_cel}")