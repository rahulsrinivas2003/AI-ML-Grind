#Unpacking -----------------------------

# def total(galleons=0, sickles=0 , knuts=0):

#     return (galleons * 17 + sickles) * 29 + knuts

# # coins =[100 , 50 ,25]

# # print(total(*coins))

# #*coins allows us to unpack every single member of the " list " to unpack into 3 separate values into the total function, this is called unpacking 

# #-----------------------------------------------------------------------------------------------------------------------------------------------------

# coins = { "knuts":25, "sickles":50, "galleons":100}

# print(total(**coins)) #for dicts its 2 asterisks cuz its sending name and values as well as in galleons= 100


# args -> variable positional arguments and kwargs -> variable amound of named/keyword arguments  -----------------------------------------------------------------------------------------------------
def f(*args , **kwargs):

    print("Postional: ", args , "Keyword Arguments: ", kwargs)


f(100,50,250,300, Rahul_Anna= 1000 ,Praful_Channa=100 )

# Keyword Arguments always follow positional arguments 