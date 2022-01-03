from sys import argv
if argv[3] == "kelvin":
kev_temp = (float(argv[1]))+ 273.15
print(f"Kelvin temperature is: {kev_temp}")

if argv[3] == "celsius":
temp_cel = (float(argv[1])) * 9 / 5 + 32
print(f"Celsius temperature is: {temp_cel}")

if argv[3] == "fehrenheit":
feh_temp = (float(argv[1])) - 273,15 
print(f'Feh temp is: {feh_temp}')

