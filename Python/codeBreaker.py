import numpy as np

def find_correct(r, g):
    for i in range(0, len(r)):
        if r[i] != g[i]:
            return False
    return True

def find_match(r, g):
    ct = 0
    for i in range(0, len(r)):
        if r[i] == g[i]:
            ct = ct + 1
    return ct

def find_close(r, g):
    ct = 0
    for i in range(0, len(r)):
        for j in range(0, len(r)):
            if g[i] == r[j]:
                ct = ct + 1
    return ct

def generate_random():
    s = set()
    r_arr = 0
    while len(s) != 3:
        r_arr = np.random.randint(100,999)
        s = set(str(r_arr))
    return str(r_arr)

def start_game():
    print("Welcome to CodeBreaker Game, the random number has been generated")
    print("Win by guessing the correct 3 digit number")
    r_arr = generate_random()
    while True:
        #print(r_arr)
        print("Your Guess: ");
        g = int(input())
        g = str(g)
        if find_correct(r_arr, g):
            print(f"WON: Guessed Correctly: {g}")
            break
        else:
            match = find_match(r_arr, g)
            if match:
                print(f"MATCH: You guessed {match} number(s) correctly in right position")
            else:
                close = find_close(r_arr, g)
                if close:
                    print(f"CLOSE: You guessed {close} number(s) correctly in wrong position")
                else:
                    print("NOPE: You guessed 0 number(s) correctly")

if __name__ == "__main__":
    start_game()
