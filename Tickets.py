import random
from read import Read
class Tickets:
    def __init__(this, name):
        this.name = name
        this.plays = Read(lambda name : f"play/{name}.txt", name).getData()
        this.indexes = this.getIndexes()
        this.Tickets = this.pickTickets()
        this.printTickets()

    def getIndexes(this):
        result = {}
        for el in range(len(this.plays)):
            element = this.plays[el][0]
            if element < 10 and element not in list(result.keys()):
                result[element] = el
        return result

    def pickFromRange(this, start, end):
        index = random.choice(this.plays[start:end])
        return index
        
    def pickTickets(this):
        play = []
        i = 1
        while i < 10:
            if i == 9:
                end = len(this.plays)
            else: 
                end = this.indexes[i+1]
            play.append(this.pickFromRange(this.indexes[i], end))
            i += 1
        return play

    def printTickets(this):
        for el in this.Tickets:
            print(el)

if __name__== "__main__":
    T = Tickets("cash5")