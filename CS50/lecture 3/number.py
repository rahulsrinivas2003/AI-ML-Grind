def main():

    x = get_int("Whats x? ")
    print(f"x is {x}")

def get_int(prompt):

    while True:
        try: #called try statement instead of a function 
            x = int(input(prompt)) # u can return x here to for more concise code but this is more clear to me
        
        except ValueError:

            print("x is not an integer") #or u can use "pass" here instead of print statement but this is more clear to me
        else:
            break  #u can simply return x here but this is more clear to me

    return x

main()