import sys

current_article_id = None
current_word = None
word_sum = 0

for line in sys.stdin:
    try:
        key, count = line.strip().split('\t', 1)
        word, article_id = key.split(',', 1)
        count = int(count)
    except ValueError as e:
        continue
    if current_article_id != article_id or current_word != word:
        if current_article_id and current_word:
            key = current_word + "," + current_article_id
            print "%s\t%d" % (key, word_sum)
            word_sum = 0
        current_article_id = article_id
        current_word = word
    word_sum += count

key = current_word + "," + current_article_id
print "%s\t%d" % (key, word_sum)