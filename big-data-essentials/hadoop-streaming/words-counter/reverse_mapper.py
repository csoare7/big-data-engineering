import sys


def main():
    for line in sys.stdin:
        try:
            word, count = line.strip().split('\t', 1)
            count = int(count)
            print("{0}\t{1}".format(count, word))
        except ValueError as e:
            raise e
            continue


if __name__ == '__main__':
    main()
