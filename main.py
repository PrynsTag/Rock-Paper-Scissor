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
        LOSE = "Sorry, but the computer chose {}".format(comp_choice)
        DRAW = "There is a draw ({})".format(comp_choice)
        WIN = "Well done. The computer chose {} and failed".format(comp_choice)

        while True:
            user_choice = input().lower()
            if comp_choice == user_choice:
                result = DRAW
            elif self.user_win[comp_choice] == user_choice:
                result = WIN
            else:
                if user_choice in self.user_win:
                    result = LOSE
                else:
                    result = "Invalid Input"

            # Exit Condition
            if user_choice == "!exit":
                print("Bye!")
                break

            print(result)


if __name__ == '__main__':
    Game().play()
