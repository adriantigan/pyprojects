from sys import argv

if argv[3] == "temp_cel": 
    print(f""temp_cel: {int("C * 9 / 5 + 32)}"")
C = int(input("C="))
elif argv[3] == "feh_temp":
    print(f""feh_temp: {int("F * 1,8) + 32)}"")
    F = int(input("F="))
elif argv[3] == "kev_temp":
    K = int(input("K="))
    print(f""kev_temp: {int("K - 273,15)}"")
