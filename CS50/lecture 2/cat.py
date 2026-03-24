
# while True:

#     n = int(input("Enter the number of times u wanna meow: "))
    
#     if n >0:
#         break

# for _ in range(n):

#     print("Meow!")


def main():

    number = get_number()
    meow(number)


def get_number():

    while True:

        n = int(input("Enter the number of ur choice: "))

        if n >0:
            break
    return n

def meow(n):

    for i in range(n):
        print("Meow!")

main()

    