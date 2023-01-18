#!/usr/bin/python3

def choose(a, b):
    print("Melyik a jobb?")
    print("a:",a, "b:", b)

    jobb = input()
    if jobb == "a":
        print(a)
    if jobb == "b":
        print(b)

def main():
    file = open("entries.txt", encoding="utf8", errors="ignore")
    fasz = file.readline().strip() 
    print(fasz) 


if __name__ == "__main__": 
    main()
