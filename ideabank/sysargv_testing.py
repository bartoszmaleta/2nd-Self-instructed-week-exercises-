import sys
# print("This is the name of the script: ", sys.argv[0])
# print("Number of arguments: ", len(sys.argv))
# print("The arguments are: ", str(sys.argv))

# print(sys.argv)
print

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print(arg)
else:
    print('No arguments provided')

print