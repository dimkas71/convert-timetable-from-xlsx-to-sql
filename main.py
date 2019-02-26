import re

CORRECT_PN = "00/0010"
INCORRECT_PN = "0d/0001"


CORRECT_PN_LIST = [
    "00/0012",
    "10/1012",
    "00/0010"
]

PN_PATTERN = "\d{2}\/\d{4}"



if (__name__ == '__main__'):

    pattern = re.compile(PN_PATTERN) 
    print(pattern.match(CORRECT_PN))
    print(pattern.match(INCORRECT_PN))
    print("Hello world")

    [print(pattern.match(x)) for x in CORRECT_PN_LIST]
