#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length <= 1:
        print("0 arguments.")
    elif length == 2:
        print(f"{length - 1} argument:")
    else:
        print(f"{length - 1} arguments:")
    for x in range(1, length):
        print(f"{x}: {sys.argv[x]}")
