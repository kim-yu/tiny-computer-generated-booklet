import random

internet_slang = {  'aab': 'average at best',
                    'aak': 'alive and kicking',
                    'aap': 'always a pleasure',
                    'abd': 'already been done',
                    'bff': 'best friends forever',
                    'bts': 'be there soon',
                    'ctn': 'cannot talk now',
                    'cye': 'check your email',
                    'diy': 'do it yourself',
                    'dnd': 'do not disturb',
                    'eom': 'end of message',
                    'etw': 'enjoy the weekend',
                    'fka': 'formerly known as',
                    'ftw': 'for the win',
                    'giy': 'google it yourself',
                    'gnd': 'girl next door',
                    'gsd': 'getting stuff done',
                    'gtb': 'go to bed',
                    'hak': 'hugs and kisses',
                    'hth': 'hope this helps',
                    'idc': "i don't care",
                    'ily': 'i love you',
                    'imo': 'in my opinion',
                    'irl': 'in real life', 
                    'jam': 'just a minute',
                    'jtc': 'join the club',
                    'jwd': 'job well done',
                    'lmk': 'let me know',
                    'lol': 'laugh out loud', 
                    'nrn': 'no reply necessary',
                    'otl': 'out to lunch',
                    'otp': 'on the phone',
                    'pir': 'parent in room',
                    'smh': 'shaking my head',
                    'tia': 'thanks in advance',
                    'tmi': 'too much information',
                    'tyt': 'take your time',
                    'wfm': 'works for me',
                    'yam': 'yet another meeting'
                }
slang = random.choice([a for a in internet_slang.keys()])
print(slang)

definition = internet_slang[slang].split()
new_definition = ''
real_definition = ''
for i in range(len(slang)):
    w = random.choice([s for s in ' '.join(internet_slang.values()).split() if s[0] == slang[i].lower() and s != definition[i] and s not in new_definition])
    new_definition += w
    real_definition += definition[i]
    if i < len(slang)-1:
        num_spaces = max(len(w), len(definition[i])) - min(len(w), len(definition[i])) + 1
        if len(w) < len(definition[i]):
            new_definition += ' ' * num_spaces
            real_definition += ' '
        else:
            new_definition += ' '
            real_definition += ' ' * num_spaces
if (random.randint(1, 2) == 1):
    print('1) ' + real_definition)
    print('2) ' + new_definition)
else:
    print('1) ' + new_definition)
    print('2) ' + real_definition)
