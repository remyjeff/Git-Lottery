from itertools import combinations
from data import inCommonN
from read import Read, write
from test import winners

class Filter:
    def __init__(this, name) -> None:
        this.name = name
        this.plays = this.getPlays()
        this.data = Read(name).getData()
        this.size = len(this.data)
        this.F = this.indexRange()

    def getPlays(this):
        lst2 = list(combinations([x for x in range(1, 36)], 5))
        lst = []
        for i in range(len(lst2)):
            if lst2[i][0] == 10:
                break
            lst.append(list(lst2[i]))
        return lst

    def commonFilter(this, myStart= 0, segment=17, common=3):
        # remove the last segments with {common} in common and then check for win. keep count of wins!
        start = myStart #this.size - segment
        count = 0
        cnt = 0
        cnt1 = 0
        while(start >= 0):
            result = []
            interest = this.data[start]
            if interest[0] < 10:
                for p1 in this.plays:
                    state = False
                    for p in this.data[start+1:start+segment]:
                        if p[0] >= 10:
                            continue
                        state = inCommonN(p1, p, common)
                        if state:
                            break
                    if not state:
                        result.append(p1)


                if winners([interest], result) == 1:
                    count += 1
                r = this.rangeFilter(result)
                if winners([interest], r) == 1:
                    cnt += 1
                rr = this.sequense(r, start+1, 7)
                if winners([interest], rr) == 1:
                    cnt1 += 1
                    write(rr, this.name)
                print(f" Result1 = {len(result)} : Count = {count} Result2 = {len(r)} : Cnt = {cnt} : Result3 : {len(rr)} cnt1: {cnt1} {interest}")



            start -= 1
        #print(count) # 2630 total
        return {"inCommon":common, "segemnt":segment, "Wins":count}

    def indexRange(this):
        result = {}
        for lines in this.data:
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
            result[k] = list(this.sortDict(v))[:-2]
        return result

    def sortDict(this, dict1):
        sorted_tuples = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = {k: v for k, v in sorted_tuples}
        return sorted_dict

    def rangeFilter(this, lst):
        result = [] 
        for l in lst:
            state = True
            for i in range(len(l)):
                if l[i] // 10 in this.F[i+1]:
                    continue
                else:
                    state = False
                    break
            if state:
                result.append(l)
        return result

    def sequenseFilter(this, lst, index, segment=3):
        count = 0
        for m in this.data[index:index+segment]:
            for i in range(len(lst)):
                if lst[i] == m[i]:
                    count += 1
                else:
                    count = 0
                if count == 2:
                    return True
        return False

    def sequense(this, lst, index, segment):
        result = []
        for l in lst:
            if not this.sequenseFilter(l, index, segment):
                result.append(l)
        return result
