from random import choice


class Game:
    def __init__(self):
        self.choice = ["rock", "paper", "scissors"]
        self.user_win = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }

    def play(self):
        return self.result(choice(self.choice))

    def result(self, comp_choice):
        LOSE = "Sorry, but the computer chose {}"
        DRAW = "There is a draw ({})"
        WIN = "Well done. The computer chose {} and failed"

        while True:
            user_choice = input().lower()
            if comp_choice == user_choice:
                result = DRAW.format(comp_choice)
            elif self.user_win[comp_choice] == user_choice:
                result = WIN.format(comp_choice)
                break
            else:
                if user_choice in self.user_win:
                    result = LOSE.format(comp_choice)
                else:
                    result = f"Wrong Input. Chose from: {', '.join(self.choice)}"
            print(result)

        print(result)


if __name__ == '__main__':
    Game().play()
