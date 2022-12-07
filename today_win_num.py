import random
from your_luck_num import*
class TodayWin(YourNumber):

    win_no = []
    def todywinFunction(self):
        your_luck_num=self.your_num_fun()

        for i in range(0, 5):
            numb = random.randint(1, 20)
            while numb in self.win_no:
                numb = random.randint(1, 20)
            self.win_no.append(numb)
        self.win_no.sort()
        res = len(set(your_luck_num) & set(self.win_no))
        print("The amount of the same numbers are :", res)
        return res

today_win = TodayWin()

