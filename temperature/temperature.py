temp_cel = input('Enter temperature: ')
fahren_temp = (float(temp_cel) * 1.8) + 32

kev_temp = (float(temp_cel)) + 273.15

new_temp = (float(temp_cel) * 0.33000 )
print(float(fahren_temp))
print(float(kev_temp))
print(float(new_temp))

"""
1.
pune sa stiu ce temperatura i fiecare si scoate input in pula mea
kev_temp = (float(argv[1])) + 273.15
print(f"Kelvin temperature is: {kev_temp}")

2.
dupa ce faci asta extinde programu sa converteasca dintr o temperatura
in alta
ex. python temperature.py 23 newton kelvin
23 de grade newton in kelvin
etc.
"""
