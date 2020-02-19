from roman_to_integer import digits

class Main:

    def __init__(self):
        self.num = {}

        self.goods = {}

        self.operand = []
        self.operator = []

    def process(self, line):
        word = line.lower().split(None)

        if not word or len(word) <= 0:
            return
            
        if len(word) > 3 and word[0] in ['glob', 'prok', 'pish', 'tegj'] and not (word[-1] == 'credits'):

            for i in word:
                if i in ['glob', 'prok', 'pish', 'tegj']:
                    self.operand.append(i)
                elif i in digits:
                    self.operator.append(digits[i])

            return
        
        if len(word) > 4 and word[-1] == 'credits' and word[-3] == 'is':
            word.pop()
            try:
                val = float(word[-1])
            except:
                return self._msg("{0} is not valid numeric value".format(word[-1]))

            word.pop()
            # print(word)
            word.pop()
            # print(word)
            g = word.pop()
            n = self._parse(word)

            self.goods[g] = val / n

            return

        if word[0:3] == ['how', 'much', 'is']:
            word = word[3:]
            if word[-1] == '?':
                word.pop()

            n = self._parse(word)

            if n < 0:
                return self._msg("{0} is not valid galatic number {1}".format(n, word))

            print(' '.join(word), 'is', n)
            
            return
        
        if word[0:4] == ['how', 'many', 'credits', 'is']:
            word = word[4:]
            if word[-1] == '?':
                word.pop()
            g = word.pop()

            if not g in self.goods:
                return self._msg("I don't know the galaxy trading good {0}".format(g))
            
            n = self._parse(word)
            if n < 0:
                return self._msg("{0} is not valid galatic number {1}".format(n, word))
            
            print(''.join(word), g.title(), "is", int((n * self.goods[g])), "Credits")
        else:
            return self._msg("I don't know idea what you talking about")

    def _parse(self, word):
        num = {self.operand[i]: self.operator[i] for i, v in enumerate(self.operand)}

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

    def _msg(self, s):
        print(s)

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
    trx = Main()

    for line in lines:
        trx.process(line)