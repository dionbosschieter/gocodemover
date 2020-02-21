import sys

from gocodemover import main
from sys import argv

if __name__ == '__main__':
    if len(argv) < 3:
        print(argv[0], "{directory for files to move} {destination output file}")
        sys.exit(1)

    main(argv[1], argv[2])