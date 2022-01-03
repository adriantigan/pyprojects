from sys import argv 



kev_temp = ((float(argv[1]))+ 273.15)
print(f"Kelvin temperature is: {kev_temp}")


temp_cel = ((float(argv[1])) * 9 / 5 + 32)
print(f"Celsius temperature is: {temp_cel}")


feh_temp = ((float(argv[1])) - 273,15) 
print(f'Feh temp is: {feh_temp}')


