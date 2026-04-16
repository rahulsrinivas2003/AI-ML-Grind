def main():

    yell("this", "is","CS50P")

def yell(*words):

    # uppercased = map(str.upper , words) #map function applies the method (upper) to every word passed in the argument
    uppercased= [word.upper() for word in words] #using list comprehensions 
    print(*uppercased)

if __name__ == "__main__":
    main()