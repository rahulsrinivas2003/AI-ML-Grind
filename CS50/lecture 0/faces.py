def  convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")

    return s


def main():

    statement = input("Enter the faces: ")
    print(convert(statement))

main()
