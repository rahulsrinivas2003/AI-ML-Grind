import argparse 

parser = argparse.ArgumentParser(description="Meow like a Cat!!")
parser.add_argument("-n", default=1, help="number of times to meow", type= int)
args = parser.parse_args()

for i in range(args.n):
    print("meow")