from nltk.corpus import words
import random

internet_slang = {  'afk': 'away from keyboard',
                    'ama': 'ask me anything',
                    'asap': 'as soon as possible',
                    'atm': 'at the moment',
                    'bff': 'best friends forever',
                    'brb': 'be right back', 
                    'btw': 'by the way', 
                    'dftba': "don't forget to be awesome",
                    'dnd': 'do not disturb',
                    'faq': 'frequently asked questions', 
                    'ftw': 'for the win',
                    'fyi': 'for your information', 
                    'gtg': 'got to go',
                    'idk': "i don't know",
                    'ily': 'i love you',
                    'imo': 'in my opinion',
                    'irl': 'in real life', 
                    'jk': 'just kidding',
                    'lmgtfy': 'let me google that for you',
                    'lmk': 'let me know',
                    'lol': 'laugh out loud', 
                    'myob': 'mind your own business',
                    'np': 'no problem',
                    'nsfw': 'not safe for work', 
                    'omw': 'on my way',
                    'rotfl': 'rolling on the floor laughing',
                    'smh': 'shaking my head',
                    'tbh': 'to be honest', 
                    'tldr': "too long didn't read",
                    'tmi': 'too much information',
                    'ttyl': 'talk to you later',
                    'ty': 'thank you',
                    'wbu': 'what about you',
                    'yolo': 'you only live once'
                }

slang = random.choice(a for a in internet_slang.keys()])
meaning = internet_slang[slang].split()

new_meaning = ''
real_meaning = ''
for i in range(len(slang)):
    word = random.choice([word for word in word.words("en-basic") if word[0] == slang[i].lower()])
    new_meaning += word
    real_meaning += meaning[i]
    if i < len(slang)-1:
        length = max(len(word), len(meaning[i])) - min(len(word), len(meaning[i])) + 1
        if len(word) < len(meaning[i]):
            new_meaning += ' ' * length
            real_meaning += ' '
        else:
            new_meaning += ' '
            real_meaning += ' ' * length

print(slang + '\n' + real_meaning + '\n' + new_meaning)
