#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    lengArg = len(sys.argv)
    if lengArg <= 1:
        print("0 arguments.")
    else:
        print(f"{lengArg - 1} argument:")
    for item in range(1, lengArg):
        print(f"{item}: {sys.argv[item]}")
