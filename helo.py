#!/usr/bin/python3
import sys
import math
 
def log2(x):
    return math.log10(x) / math.log10(2)

def is_pow2(x):
    y = log2(x)
    return y == int(y)

def main():

    if len(sys.argv) < 2:
        print("specify file")
        quit()
    fnam = sys.argv[1]
    file = open(fnam, encoding="utf-8", errors="ignore")

    members = file.read().splitlines()
    file.close()

    winner = game(members, choose)
    print("Nyert:", winner)

def normalize(members):
    #TODO: implement normalize
    return members

def game(actuals, chooser):

    assert(len(actuals) > 0)
    actuals = normalize(actuals)
    assert(is_pow2(len(actuals)))

    while True:
        if len(actuals) == 1:
            break
        else:
            actuals = perform_round(actuals, chooser)

    return actuals[0]

def choose(a, b):

    print("Melyik a jobb?")
    print("a:",a, "b:", b)

    while True:

        jobb = input()

        if jobb == "a":
            return a
        if jobb == "b":
            return b
        if jobb == "q":
            return None
        print("a vagy b")
    


    
def perform_round(parties, chooser):

    round_winners = []
    for match_num in range(int(len(parties) / 2)):

        p1 = parties[int(match_num * 2)]
        p2 = parties[int(match_num * 2 + 1)]
        winner = chooser(p1, p2)

        if winner is None:
            print("Aborted")
            quit()

        round_winners.append(winner)
        
    return round_winners


if __name__ == "__main__": 
    main()