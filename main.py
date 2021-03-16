from random import choice


class Game:
    def __init__(self):
        self.choice = ["rock", "paper", "scissors"]
        self.user_win = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }
        self.player_name = None
        self.leaderBoard = {}

    def greet_player(self):
        self.player_name = input("Enter your name: ")
        print(f"Hello, {self.player_name}")

    def read_file(self):
        with open("rating.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(" ")
                self.leaderBoard[key] = int(value)

    def play(self):
        self.greet_player()
        self.read_file()
        # Check if player has existing score, 0 if not
        SCORE = self.leaderBoard[self.player_name] if self.player_name in self.leaderBoard.keys() else 0
        LOSE = "Sorry, but the computer chose {}"
        DRAW = "There is a draw ({})"
        WIN = "Well done. The computer chose {} and failed"

        while True:
            user_choice = input().lower()
            comp_choice = choice(self.choice)

            if comp_choice == user_choice:
                result = DRAW.format(comp_choice)
                SCORE += 50
            elif self.user_win[comp_choice] == user_choice:
                result = WIN.format(comp_choice)
                SCORE += 100
            elif user_choice == "!rating":
                result = self.rating()
            elif user_choice == "!leaderboard":
                result = self.score_board()
            else:
                if user_choice in self.user_win:
                    result = LOSE.format(comp_choice)
                else:
                    result = "Invalid Input"

            # Exit Condition
            if user_choice == "!exit":
                print("Bye!")
                break

            self.leaderBoard[self.player_name] = SCORE
            print(result)

    def rock_paper_scissor(self):
        

    def score_board(self):
        sorted_dict = dict(sorted(self.leaderBoard.items(),
                                  key=lambda item: item[1],
                                  reverse=True))
        scores, counter = [], 0

        for key, value in sorted_dict.items():
            counter += 1
            scores.append(f"{counter}. {key}: {value}")

        return '\n'.join(scores)

    def rating(self):
        if self.player_name in self.leaderBoard.keys():
            return f"your rating: {self.leaderBoard[self.player_name]}"
        else:
            return f"your rating: 0"


if __name__ == '__main__':
    Game().play()
