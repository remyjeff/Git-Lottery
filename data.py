
def inCommonN(interest, p, n):
        count = 0
        for el in interest:
            if el in p:
                count += 1
        return count >= n

class Data:
    def __init__(this, data) -> None:
        this.data = data
        this.size = len(data)

    def sortDict(this, dict1):
        sorted_tuples = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = {k: v for k, v in sorted_tuples}
        return sorted_dict

    def sumStatistic(this):
        result = {}
        for lines in this.data:
            s = sum(lines) // 10
            if s in list(result.keys()):
                result[s] += 1
            else:
                result[s] = 1
        return this.sortDict(result)

    def diffStatistic(this):
        result = {}
        for lines in this.data:
            s = (lines[-1] - lines[0]) // 10 
            if s in list(result.keys()):
                result[s] += 1
            else:
                result[s] = 1
        return this.sortDict(result)

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
        for lines in this.data:
            key = this.getParity(lines)
            if key in list(result.keys()):
                result[key] += 1
            else:
                result[key] = 1
        return this.sortDict(result)

    def inCommonN(this, interest, p, n):
        count = 0
        for el in interest:
            if el in p:
                count += 1
        return count >= n
    # segment is the the amount of past days to compare to. 
    def lastNInCommon(this, segment=3, common=3):
        start = this.size - segment
        inIt = 0
        notInIt = 0
        while(start > 0):
            interest = this.data[start]
            state = False
            for p in this.data[start+1:start+segment]:
                state = inCommonN(interest, p, common)
                if state:
                    break
            if state:
                inIt += 1
            else:
                notInIt +=1
            start -= 1
        return {"inCommon":common, "segemnt":segment, "inIt":inIt, "notInIt":notInIt, "ratio":notInIt/(notInIt+inIt)}

    def getIndexPlayRange(this):
        result = {}
        for line in this.data:
            if result.keys().__contains__(line[0]):
                result[line[0]] += 1
            else:
                c = result.setdefault(line[0], 1)
        sumIt = 0
        for i in range(1,36):
            try:
                #print(f"{i} : {result[i]}")
                if i < 10:
                    sumIt += result[i]
            except:
                pass
        print(result)
        print(f"Ratio : {sumIt} / {this.size} = {sumIt/this.size}")

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

    def sequense(this, n):
        start = len(this.data) - n
        cnt = 0
        while(start > 0):
            if this.sequenseFilter(this.data[start-1], start, n):
                cnt += 1
            start -= 1
        print("cnt : ", cnt)


    def HowManyInCommonWithLastTwo(this, index):
        l = this.data[index+1]
        m = this.data[index+2]
        temp = []
        for el in l:
            if el not in temp:
                temp.append(el)
        for el in m:
            if el not in temp:
                temp.append(el)
        return inCommonN(this.data[index], temp, 3)
