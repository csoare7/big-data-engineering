import sys

for line in sys.stdin:
    try:
        key, word_sum = line.split('\t', 1)
        word, article_id = key.split(',', 1)
    except ValueError as e:
        continue
    value = word + "," + word_sum
    print '%s\t%s' % (article_id, value)