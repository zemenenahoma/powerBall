from colorama import init, Fore, Style

from  utilts import  *

init()
# from utility1 import *
from today_win_num import *


# from operator import eq
class MainAction(TodayWin):
    def calculatingFun(self):
        res = self.todywinFunction()
        comf = self.you_luck_num
        com2 = self.win_no

        not_in_list_one = [str(b) for b in comf]
        lucky_num = "   ".join(not_in_list_one)

        notinlist = [str(b) for b in com2]
        tody_num = "   ".join(notinlist)

        # appending the the power ball to the number list(your lucky number and today win number)

        powerBall = random.randint(1, 10)
        #
        goldNum = random.randint(1, 10)

        print(f" today's lucky numbers are: {blue}  {tody_num} {yellow} {goldNum}")
        print(f"your lucky numbers are :{blue} {lucky_num} {yellow} {powerBall} ")

        if powerBall == goldNum and res == 0:
            print("You got $4 ")
        elif powerBall == goldNum and res == 1:
            print("You got $4 ")
        elif powerBall == goldNum and res == 2:
            print("You win $7")
        elif powerBall != goldNum and res == 3:
            print("you got $7 ")
        elif powerBall == goldNum and res == 3:
            print("You got 100$")
        elif powerBall != goldNum and res == 4:
            print("You got $100 ")
        elif powerBall == goldNum and res == 4:
            print("You got $10000 ")
        elif powerBall != goldNum and res == 5:
            print("you got $1000000")
        elif powerBall == goldNum and res == 5:
            print("you got $324,000,000 ")
        else:
            print("Ooops Try again! ")
        return True



