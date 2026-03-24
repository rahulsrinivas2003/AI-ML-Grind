def main():

    print_square(3)

def print_square(size):

    #For every row
    for i in range(size):

        #Print # for every column in that row
        for j in range(size):

            print("#", end="")

        print() #Move to the next line after printing all columns in a row

main()