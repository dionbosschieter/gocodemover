import os
import glob


def main(source, destination):
    files_to_concat = glob.glob(source + os.sep + "*.go")
    print("Concattenating files", files_to_concat)

    for file in files_to_concat:
        lines = []
        with open(file) as f:
            lines = f.readlines()

        for line in lines:
            if line.find('package domain') != -1:
                print('found package line')
                continue
            print(line)