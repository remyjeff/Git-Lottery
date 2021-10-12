from read import Read
from data import Data
from test import Test
from filter import Filter

class Run:
    def __init__(this) -> None:
        this.files = ["cash5", "4life", "lotto", "mega", "power"]
        this.R = Read(this.files[0])
        this.D = Data(this.R.getData())
        print(this.D.lastNInCommon(17, 3))
        this.D.getIndexPlayRange()

if __name__ == "__main__":
    F = Filter("cash5")
    F.commonFilter()