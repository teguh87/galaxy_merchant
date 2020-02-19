# galaxy_merchant
Hiring test for bitdna

## introduction 
This project porposed for simulating transfer transaction from individual to individual
the transcaction follow sum similar convertion to the roman numerals

the roman consist only seven numbers:
````
digits = {
    'i': 1,
    'v': 5,
    'x': 10,
    'l': 50,
    'c': 100,
    'd': 500,
    'm': 1000
}

````

# Design

Numbers are formed by combining symbols together and adding the values. For example, MMVI is 1000 + 1000 + 5 + 1 = 2006. Generally, symbols are placed in order of value, starting with the largest values. When smaller values precede larger values, the smaller values are subtracted from the larger values, and the result is added to the total. For example MCMXLIV = 1000 + (1000 − 100) + (50 − 10) + (5 − 1) = 1944.

The symbols "I", "X", "C", and "M" can be repeated three times in succession, but no more. (They may appear four times if the third and fourth are separated by a smaller value, such as XXXIX.) "D", "L", and "V" can never be repeated.

"I" can be subtracted from "V" and "X" only. "X" can be subtracted from "L" and "C" only. "C" can be subtracted from "D" and "M" only. "V", "L", and "D" can never be subtracted.
Only one small-value symbol may be subtracted from any large-value symbol.

so we could using this kind approachment:

```
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

```

A number written in Arabic numerals can be broken into digits. For example, 1903 is composed of 1, 9, 0, and 3. To write the Roman numeral, each of the non-zero digits should be treated separately.


## test application

Scenario for the test is based on what been determained by the tester 
it have to consist some lines for picturing the transaction 
accured.

```
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


```

# How to run script

For runing this script you must have python install in your machine (PC)
and if you don't have you must install it. Then you clone the repository and then 
enter the directory

Pleas run this comman for running this script

```
python main.py

```

## Result

if you run command above it sould be has result like this:

```
pish tegj glob glob is 42
globprok Silver is 68 Credits
globprok Gold is 57800 Credits
globprok Iron is 782 Credits
I don't know idea what you talking about

```