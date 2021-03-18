from dataclasses import dataclass
from random import choice


@dataclass
class Player:
    username: str
    score: int = 0

    def __repr__(self):
        return f"'{self.username}': {self.score}"


class Game:
    def __init__(self):
        self.player = Player("")
        self.leaderBoard = {}

    def greet_player(self):
        self.player.username = input("Enter your name: ")
        self.leaderBoard[self.player.username] = self.player.score
        print(f"Hello, {self.player.username}")

    def read_file(self):
        with open("rating.txt", "r") as file:
            for line in file:
                player = Player(*line.strip().split(" "))
                self.leaderBoard[player.username] = int(player.score)

                if self.player.username == player.username:
                    self.player.score = int(player.score)

    def command(self, user):
        if user == "!rating":
            result = f"your rating: {self.player}"
        elif user == "!leaderboard":
            result = self.score_board()
        elif user == "!export":
            result = self.export_score()
        else:
            result = "Invalid Input"

        print(result)

    def export_score(self):
        file_name = input("Specify the name of file (name.txt): ")
        with open(file_name, "w") as file:
            for key, value in self.leaderBoard.items():
                file.write(f"{key} {value}\n")

        return "Score saved!"

    def play(self):
        self.greet_player()
        self.read_file()
        option = ["rock", "paper", "scissors"]

        while True:
            user_choice = input().lower()
            comp_choice = choice(option)

            # Exit Condition
            if user_choice == "!exit":
                print("Bye!")
                break
            elif user_choice in option:
                self.rock_paper_scissor(user_choice, comp_choice)
            else:
                self.command(user_choice)

    def rock_paper_scissor(self, user, computer):
        user_win = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }
        LOSE = "Sorry, but the computer chose {}".format(computer)
        DRAW = "There is a draw ({})".format(computer)
        WIN = "Well done. The computer chose {} and failed".format(computer)

        if computer == user:
            result = DRAW
            self.player.score += 50
        elif user_win[computer] == user:
            result = WIN
            self.player.score += 100
        else:
            result = LOSE

        self.leaderBoard[self.player.username] = self.player.score
        print(result)

    def score_board(self):
        sorted_dict = dict(sorted(self.leaderBoard.items(),
                                  key=lambda item: item[1],
                                  reverse=True))
        self.leaderBoard = sorted_dict
        scores, counter = [], 0

        for key, value in sorted_dict.items():
            counter += 1
            scores.append(f"{counter}. {key}: {value}")

        return '\n'.join(scores)


if __name__ == '__main__':
    Game().play()
