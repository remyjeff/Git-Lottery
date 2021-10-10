
def winners(win, plays):
        wins = 0
        for w in win:
            if w in plays:
                wins += 1
        #print(wins)
        return wins

class Test:
    def __init__(this, name) -> None:
        this.name = name

    def winners(this, win, plays):
        wins = 0
        for w in win:
            if w in plays:
                wins += 1
        #print(wins)
        return wins