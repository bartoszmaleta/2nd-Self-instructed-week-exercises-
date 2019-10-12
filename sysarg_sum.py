import sys

if len(sys.argv) > 1:
    total = sum(int(arg) for arg in sys.argv[1:] if arg.isdigit())
    print('Total is:' + total)
else:
    print('No arguments provided')