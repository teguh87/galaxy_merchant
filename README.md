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

For runing this script you have to python inside your machine (PC)
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