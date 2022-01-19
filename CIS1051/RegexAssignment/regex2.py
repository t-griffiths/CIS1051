#REGEX 2
#THOMAS GRIFFITHS


#1
"""
.* matches between zero and unlimited times
.? matches between zero and one times
"""

import re

#2
def namesearch():
    names = "Satoshi Nakamoto Alice NakamotO RoboCop Nakamoto satoshi Nakamoto Mr. Nakamoto Nakamoto Satoshi nakamoto"
    rule = re.compile(r"[A-Z][a-z]* Nakamoto")

    for line in re.findall(rule,names):
        print(line)

#3
def numsearch():
    nums = "twenty-two fourty-three fifty-four seventy-five ninety-six"
    rule = re.compile(r'[a-z]*-[a-z]*')
    for line in re.findall(rule,nums):
        print(line)

#4
def dollarsearch():
    dollars = "$100.00 $10,000.00 $1234 $5000.00 $1,000,000"
    rule = re.compile(r'\$\S*')

    for line in re.findall(rule,dollars):
        print(line)

namesearch()
numsearch()
dollarsearch()
