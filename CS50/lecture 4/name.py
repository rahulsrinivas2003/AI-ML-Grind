import sys
#sys is a module that provides access to input variables in the cli on the same line as the program name 

#for example: python name.py Rahul 

if (len(sys.argv) < 2):

    sys.exit("Too few arguments")

# elif (len(sys.argv) > 2):

#     sys.exit("Too many arguments")

# print("hello my name is, " ,sys.argv[1])

for arg in sys.argv[1:]:
    print("hello my name is: ",arg)

