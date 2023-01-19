#!/usr/bin/python3
import sys

def main():

    if len(sys.argv) < 2:
        print("specify file")
        quit()
    fnam = sys.argv[1]
    file = open(fnam, encoding="utf-8", errors="ignore")

    members = file.read().splitlines()
    file.close()

    winner = game(members, fake_choose)
    print("Nyert:", winner)

def game(actuals, chooser):

    assert(len(actuals) > 0)

    while True:
        nexts = perform_round(actuals, chooser)
        if len(nexts) == 1:
            break
        else:
            actuals = nexts

    return nexts[0]

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