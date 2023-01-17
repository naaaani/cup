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
    choose("lo", "lofasz")
    choose("kutya", "macska")

if __name__ == "__main__": 
    main()