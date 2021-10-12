
def write(lst, name):
        if len(lst) == 0:
            print(f"There is nothing to write for {name}")
            return
        f = open(f"play/{name}.txt", 'w')
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

class Read:
    def __init__(this, fPath, fileName) -> None:
        this.name = fileName
        this.fPath = fPath
        this.data = []
        this.read()
        this.convertToInt()
        this.size = len(this.data)

    def read(this):
        f = open(this.fPath(this.name), "r")
        lines = f.read().strip("")
        lines = lines.split('\n')
        final = []
        for line in lines:
            if line != '':
                li = line.split(" ")
            final.append(li)
        f.close()
        this.data = final
        #this.convertToInt()

    def convertToInt(this):
        result = []
        for line in this.data:
            temp = []
            for n in line:
                temp.append(int(n))
            result.append(temp)
        this.data = result

    def getData(this):
        return this.data

    