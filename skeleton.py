
import operator
from collections import OrderedDict
from itertools import combinations

class skeleton:
    def __init__(this, name, range) -> None:
        print("Running ", name)
        this.name = name
        this.range = range
        this.oldData = []
        this.testData = []
        this.read()
        this.size = len(this.oldData)
        this.convertToInt()
        this.sumStat = this.sumStatistic()
        print("Sum:\n", this.sumStat)
        this.diffStat = this.diffStatistic
        print("Diff:\n", this.diffStat)
        this.indexRangeValues = this.indexRange()
        print("IndexRange:\n", this.indexRange)
        this.parityValue = this.parity()
        print("Parity:\n")

        if name == "cash5":
            this.percent = 0.60
            this.commonSeq = 4
            this.common = 1
        else:
            this.percent = 0.50
            this.commonSeq = 3
            this.common = 3
        
        this.toPlay = []
        this.greatFilter()
        this.write(this.toPlay)
        #this.runner()

    def read(this):
        f = open(f"games/{this.name}.txt", "r")
        lines = f.read().strip("")
        lines = lines.split('\n')
        final = []
        for line in lines:
            li = line.split(" ")
            final.append(li)
        f.close()
        this.oldData = final
        #return final

    def write(this, lst):
        if len(lst) == 0:
            print(f"There is nothing to write for {this.name}")
            return
        f = open(f"play/{this.name}.txt", 'w')
        if type(lst[0]) == list:
            for p in lst:
                s = ""
                for i in range(len(p)):
                    if i == (len(p) -1):
                        s += str(p[i])+"\n"
                    else:
                        s += str(p[i])+" "
                f.write(s)
        else:
            s = ""
            for i in range(len(lst)):
                if i == (len(lst) -1):
                    s += " "+str(lst[i])+"\n"
                else:
                    s += " "+str(lst[i])
            f.write(s)
        f.close()

    def convertToInt(this):
        result = []
        for line in this.oldData:
            temp = []
            for n in line:
                temp.append(int(n))
            result.append(temp)
        this.oldData = result
        #this.testData = result[]
        #return result

    def sumStatistic(this):
        result = {}
        for lines in this.oldData:
            s = sum(lines) // 10
            if s in list(result.keys()):
                result[s] += 1
            else:
                result[s] = 1
        return this.sortDict(result)

    def diffStatistic(this):
        result = {}
        for lines in this.oldData:
            s = (lines[-1] - lines[0]) // 10 
            if s in list(result.keys()):
                result[s] += 1
            else:
                result[s] = 1
        return this.sortDict(result)

    def indexRange(this):
        result = {}
        for lines in this.oldData:
            i = 1
            for l in lines:
                if i in list(result.keys()):
                    if (l //10) in list(result[i].keys()):
                        result[i][l//10] += 1
                    else:
                        result[i][l//10] = 1
                else:
                    result[i] = {}    
                i += 1
        for k, v in result.items():
            result[k] = this.sortDict(v)
        return result
    
    def getParity(this, lines):
        key = ""
        for l in lines:
                if l % 2 == 1:
                    key += "1"
                else:
                    key += "0"
        return key

    def parity(this):
        result = {}
        for lines in this.oldData:
            key = this.getParity(lines)
            if key in list(result.keys()):
                result[key] += 1
            else:
                result[key] = 1
        return this.sortDict(result)

    def sortDict(this, dict1):
        sorted_tuples = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = {k: v for k, v in sorted_tuples}
        return sorted_dict

    def get90Percent(this, json):
        sum = 0
        lst = list(json)
        result = []
        for k in lst:
            if sum >= int(this.size * this.percent):
                return result
            else:
                sum += json[k]
                result.append(k)
        return result

    def isInRange(this, line, indexes):
        i = 0
        while i < len(line):
            if (line[i] // 10) in indexes[i+1]:
                i += 1
                continue
            else:
                return False
        return True

    def greatFilter(this):
        diffs = this.get90Percent(this.diffStat)
        sums = this.get90Percent(this.sumStat)
        indexes = {}
        for k, v in this.indexRangeValues.items():
            indexes[k] = this.get90Percent(v)
        parities = this.get90Percent(this.parityValue)
        result = []
        lst2 = list(combinations([x for x in range(1, this.range)], len(this.oldData[-1])))
        lst = []
        for i in range(len(lst2)):
            if lst2[i][0] == 10:
                break
            lst.append(list(lst2[i]))

        for line in lst:
            if (sum(line) // 10) not in sums:
                continue
            elif ((line[-1] - line[0]) // 10) not in diffs:
                continue
            elif (this.getParity(line) not in parities):
                continue
            elif not this.isInRange(line, indexes):
                continue
            elif line in this.oldData:
                continue
            elif this.inCommon(line, this.common):
                continue
            elif this.inCommonSequence(line, this.commonSeq):
                continue
            else:
                result.append(line)
        count = 0
        for l in this.testData:
            if l in result:
                count += 1
        #print(f"Wins: {count} / {len(this.testData)} = {count/len(this.testData)}")
       # print(f"Wins: {count} / {len(result)} = {count/len(result)}")
        this.toPlay = result
        return count / len(result), len(result)
        #return result
    
    def inCommon(this, l, s):
        for m in this.oldData[:s]:
            count = 0
            for n in m:
                if n in l:
                    count += 1
                if count == 3:
                    return True
        return False

    def inCommonSequence(this, lst, n):
        count = 0
        for m in this.oldData[:n]:
            for i in range(len(lst)):
                if lst[i] == m[i]:
                    count += 1
                else:
                    count = 0
                if count == 2:
                    return True
        return False

    def positionSelection(this, line, last):
        for l in this.oldData[:last]:
            if line[1] == l[1] and line[-2] == l[-2]:
                return True
        return False

    def runner(this):
        percent = [x / 20 for x in range(12, 19)]
        common = [x for x in range(1, 20)]
        commonSeq = [x for x in range(1, 20)]
        values = []
        maxx = 0
        trial = 0
        for p in percent:
            this.percent = p
            for c in common:
                this.common = c
                for cs in commonSeq:
                    this.commonSeq = cs
                    s, x = this.greatFilter()
                    if s > maxx:
                        values = [p, c, cs]
                        maxx = s
                    else:
                        break
                    trial += 1
                    print(f"Trial : {trial} current max : {maxx} Trying: {[this.percent, this.common, this.commonSeq]}")
                print(f"Max : {maxx} length : {x} Values : {values}")
        print(f"Max : {maxx} length : {x} Values : {values}")

if __name__ == "__main__":
    s = skeleton("cash5", 36)
    s = skeleton("4life", 49)
    s = skeleton("lotto", 45)
    s = skeleton("mega", 71)
    s = skeleton("power", 70)