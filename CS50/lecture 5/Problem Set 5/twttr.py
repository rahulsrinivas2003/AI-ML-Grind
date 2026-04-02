
def main():

    statement = input("Input: ")


    print(shorten(statement))

def shorten(word):

    result = ""
    for letter in word:
        if letter.lower() not in "aeiou":
            result += letter
    return result

if __name__ == "__main__":
    main()
