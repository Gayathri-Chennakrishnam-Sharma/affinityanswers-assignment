from better_profanity import profanity
file = open('./paragraph.txt', 'r')
paragraph = file.read()
censored_text = profanity.censor(paragraph, '*')
counter=0
for word in paragraph.split():
    if profanity.contains_profanity(word):
        counter += 1
        print('entered')
print(paragraph, '\n', censored_text, '\n', counter)