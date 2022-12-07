#Taking lottery numbers

import random
class YourNumber:
    you_luck_num = []
    def your_num_fun(self):

        for i in range(0, 5):
            your_luck = random.randint(1, 20)

            #THE RANDOM NUMBER SHOULD NOT BE DUBLICATED USE WHILE LOOP

            while your_luck in self.you_luck_num:
                your_luck = random.randint(1, 20)
            self.you_luck_num.append(your_luck)
        self.you_luck_num.sort()
        return self.you_luck_num


today_win = YourNumber()





