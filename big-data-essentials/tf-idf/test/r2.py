import sys

article_word_count = 0
current_article_id = None

article_words = {}
article_word_counts = {}
val = []

for line in sys.stdin:
    try:
        article_id, value = line.strip().split('\t', 1)
        word, word_sum = value.split(',', 1)
    except ValueError as e:
        continue

    if current_article_id != article_id:
        if current_article_id:
            article_word_counts[current_article_id] = article_word_count
            article_word_count = 0
        current_article_id = article_id
    try:
        article_word_count += int(word_sum)
        if article_id in article_words.keys():
            temp_list = article_words[article_id]
            temp_list.append(word + "\t" + word_sum)
            article_words[article_id] = temp_list
        else:
            temp_list = []
            temp_list.append(word + "\t" + word_sum) 
            article_words[article_id] = temp_list
    except:
        continue
article_word_counts[current_article_id] = article_word_count

for key in article_words.keys():
    items = article_words[key]
    for item in items:
        word, word_sum = item.strip().split("\t", 1)
        _key = word + "," + key
        _value = word_sum + "," + str(article_word_counts[key])
        print '%s\t%s' % (_key, _value) 