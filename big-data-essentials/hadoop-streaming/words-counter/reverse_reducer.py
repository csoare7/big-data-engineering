import sys


for line in sys.stdin:
    try:
        count, word = line.strip().split('\t', 1)
        count = int(count)
        print("{0}\t{1}".format(word, count))
    except ValueError as e:
        continue
