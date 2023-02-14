import random, time, os
def main():
    secret = random.randrange(1, 101)
    print("Can you guess my secret number?")
    n = input("Guess:")
    while n.isdigit()==False:
        print("n=[0,100]")
        print("")
        n=input("Guess:")
    t = 1
    n=float(n)
    if n>100:
        print("Your number must be less than 100.")
        n = input("Guess:")
        while n.isdigit() == False:
            print("n=[0,100]")
            print("")
            n = input("Guess:")
        n=float(n)
    while n!=secret:
        if n>secret:
            print("HIGH ({}º try.)".format(t))
            time.sleep(0.5)
            print("")
            n = input("Try again:")
            while n.isdigit() == False:
                print("n=[0,100]")
                time.sleep(0.5)
                print("")
                n = input("Try again:")
            n=float(n)
            t +=1
        elif n<secret:
            print("LOW ({}º try.)".format(t))
            time.sleep(0.5)
            print("")
            n = input("Try again:")
            while n.isdigit() == False:
                print("n=[0,100]")
                time.sleep(0.5)
                print("")
                n = input("Try again:")
            n=float(n)
            t +=1
    os.system('clear')
    print("{} IS THE SECRET NUMBER! (Total tries: {})".format(secret, t))
    time.sleep(5)

main()
