import sys

digits = {
    'i': 1,
    'v': 5,
    'x': 10,
    'l': 50,
    'c': 100,
    'd': 500,
    'm': 1000
}

num = {}

goods = {}

operand = []
operator = []

def msg(message):
    print(message)

def parse(word):

    num = {operand[i]: operator[i] for i, v in enumerate(operand)}

    n = 0
    try:
        dig = [num[i] for i in word]
    except:
        return -1
    while dig:
        d = dig.pop(0)
        if dig and dig[0] > d:
            n -= d
        else:
            n += d
    return n

def process(line):
    word = line.lower().split(None)

    if not word or len(word) <= 0:
        return
        
    if len(word) > 3 and word[0] in ['glob', 'prok', 'pish', 'tegj'] and not (word[-1] == 'credits'):

        for i in word:
            if i in ['glob', 'prok', 'pish', 'tegj']:
                operand.append(i)
            elif i in digits:
                operator.append(digits[i])

        return
    
    if len(word) > 4 and word[-1] == 'credits' and word[-3] == 'is':
        word.pop()
        try:
            val = float(word[-1])
        except:
            return msg("{0} is not valid numeric value".format(word[-1]))

        word.pop()
        word.pop()

        g = word.pop()
        n = parse(word)

        goods[g] = val / n

        return

    if word[0:3] == ['how', 'much', 'is']:
        word = word[3:]
        if word[-1] == '?':
            word.pop()

        n = parse(word)

        if n < 0:
            return msg("{0} is not valid galatic number {1}".format(n, word))

        print(' '.join(word), 'is', n)
        
        return
    
    if word[0:4] == ['how', 'many', 'credits', 'is']:
        word = word[4:]
        if word[-1] == '?':
            word.pop()
        g = word.pop()

        if not g in goods:
            return msg("I don't know the galaxy trading good {0}".format(g))
        
        n = parse(word)
        if n < 0:
            return msg("{0} is not valid galatic number {1}".format(n, word))
        
        print(''.join(word), g.title(), "is", int((n * goods[g])), "Credits")
    else:
        return msg("I don't know idea what you talking about")

if __name__ == "__main__":
    lines = [
        'glob is I prok is V pish is X tegj is L',
        'glob glob Silver is 34 Credits',
        'glob prok Gold is 57800 Credits',
        'pish pish Iron is 3910 Credits',
        'how much is pish tegj glob glob ?',
        'how many Credits is glob prok Silver ?',
        'how many Credits is glob prok Gold ?',
        'how many Credits is glob prok Iron ?',
        'how much wood could a woodchuck chuck if a woodchuck could chuck wood ?'
    ]

    for line in lines:
        process(line)