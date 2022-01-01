from sys import argv

if argv[3] == "cel": 

    print("cel: {int(argv[1]) * 9 / 5 + 32)}")
elif argv[3] == "feh":

    print(f"feh: {{int(argv[1]) * 1,8) + 32)}}")

elif argv[3] == "kev":

    print(f"kev: {{int(argv[1]) - 273,15)}}")

print(argv)