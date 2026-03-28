while True:

    try:

        fraction = input("Enter the fraction of fuel left : ")

        x,y = fraction.split("/")


        x = int(x)
        y = int(y)

        if x > y:
            continue
        if x < 0 or y <0:

            continue


        fuel = round(x/y * 100)



        if fuel <= 1:

            print("E")

        elif 100 >= fuel >= 99:

            print("F")

        else:

            print(f"{fuel}%")

    except ValueError:

        pass
    except ZeroDivisionError:

        pass

    else:
        break





