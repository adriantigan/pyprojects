from sys import argv 

"""
1. Cand ai ceva cu virgula, pui punct nu virgula,
gen pe linia 25 ai facut corect :)), pe linia 33 nu
ex.
feh_temp = ((float(argv[1])) - 273,15) 
|
feh_temp = ((float(argv[1])) - 273.15) 

2. Ce ii "Feh temp" -  mereu cand
termini un cod si il rulezi intreaba-te daca ai folosi
un program de pe net si asta ar fi rezultatul, daca l-ai
folosi din nou sau daca esti multumit de functionalitate,
interfata etc. si incorporeaza la tine in cod, asa iti faci
obiceiuri bune

3. La calcule/formule parantezele is ca la matematica,
gen nu e nevoie de paranteze externe neaparat
ex.
kev_temp = ((float(argv[1]))+ 273.15)
|
kev_temp = float(argv[1])+ 273.15
"""
kev_temp = ((float(argv[1]))+ 273.15)
print(f"Kelvin temperature is: {kev_temp}")


celsius_temperature = ((float(argv[1])) * 9 / 5 + 32)
print(f"Celsius temperature is: {celsius_temperature}")


fahrenheit_temperature = ((float(argv[1])) - 273.15) 
print(f'Fahrenheit temp is: {fahrenheit_temperature}')

"""
De facut:
1. Schimba formulele alea sa presupui ca inputu
e celsius, si din celsius tranformi in restul

2. Mai ia un argument de la user care specifica in
ce temperatura sa fie tranformat numarul
ex.
python temperature.py 23 kelvin

Presupui ca la punctul 1 ca 23 e celsius
si o tranformi in kelvin (folosesti "if" la
treaba asta) - sa ai si optiunea de "all"
unde ii printezi la om din celsius in toate

----------------------------
De notat
----------------------------
Trebuie sa ai 2 commituri
- un commit cu schimbarea de la punctu 1
- un commit cu schimbarea de la punctu 2

Sablon Mesaj:
"id1: celsius temperature standard"
"id2: user temperature options added"
"""
