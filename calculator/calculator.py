from sys import argv


if argv[3] == "sum": 
    print(f"sum: {int(argv[1]) + int(argv[2])}")
elif argv[3] == "scd":
    print(f"scd: {int(argv[1]) - int(argv[2])}")
elif argv[3] == "imp":
    print(f"imp: {int(argv[1]) / int(argv[2])}")
elif argv[3] == "mult":
    print(f"mult: {int(argv[1]) * int(argv[2])}")

print(argv)