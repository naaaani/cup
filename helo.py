#!/usr/bin/python3

def main():

    file = open("entries.txt", encoding="utf-8", errors="ignore")
    actuals = file.read().splitlines()
    file.close()

    while True:
        nexts = perform_round(actuals)
        if len(nexts) == 1:
            break
        else:
            actuals = nexts

    print(nexts[0])

def choose(a, b):
    print("Melyik a jobb?")
    print("a:",a, "b:", b)

    jobb = input()
    if jobb == "a":
        return a
    if jobb == "b":
        return b
    
    return None

def fake_choose(p1, p2):
    return p1
    
def perform_round(parties):

    round_winners = []
    for match_num in range(int(len(parties) / 2)):
        p1 = parties[int(match_num * 2)]
        p2 = parties[int(match_num * 2 + 1)]
        winner = choose(p1, p2)
        round_winners.append(winner)
    return round_winners





if __name__ == "__main__": 
    main()