def main():

    n = int(input("Whats n ?: "))
    for s in sheep(n):
        print(s)

def sheep(n):

    for i in range(n):
        yield "🐑" * i #the yield keyword here is called a generator which allows to return sheeps into smaller chuncks ..efficient if ur n = 100000

if __name__ == "__main__":
    main()