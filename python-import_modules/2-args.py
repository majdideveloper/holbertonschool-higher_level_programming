#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    lengArg = len(sys.argv)
    if lengArg <= 1:
        print("0 arguments.")
    elif lengArg == 2:
    print(f"{lengArg - 1} argument:")
    else:
        print(f"{lengArg - 1} arguments:")
    for item in range(1, lengArg):
        print(f"{item}: {sys.argv[item]}")
