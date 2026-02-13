
import sys

if len(sys.argv) > 1:
    full_string = " ".join(sys.argv[1:])
        
    print(full_string.upper())
else:
    print("none")