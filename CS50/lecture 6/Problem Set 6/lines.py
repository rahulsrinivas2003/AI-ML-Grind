import sys

def main():

    if len(sys.argv) < 2:

        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif not sys.argv[1].endswith(".py"):

        sys.exit("Not a Python file")



    lines = get_lines(sys.argv[1])
    print(lines)


def get_lines(x):

    count = 0

    with open(x) as file:

        try:

            for line in file:

                if line.strip() == "":
                    continue

                if line.strip().startswith("#"):

                    continue
                else:
                    count+=1

        except FileNotFoundError:

            sys.exit("File does not exist")

    return count

if __name__ == "__main__":

    main()




