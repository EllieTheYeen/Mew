import sys


def fancylist(l):
    return ", ".join(tuple(l[:-2]) + (" and ".join(l[-2:]),))


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("*Mews softly*")
    else:
        print(f"*Mews softly at {fancylist(args)}*")


if __name__ == "__main__":
    main()
