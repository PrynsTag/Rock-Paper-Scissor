from random import choice


class Game:
    def __init__(self):
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

    def command(self, user):
        if user == "!rating":
            result = self.rating()
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

        # Check if player has existing score, 0 if not
        SCORE = self.leaderBoard[self.player_name] if self.player_name in self.leaderBoard.keys() else 0

        if computer == user:
            result = DRAW
            SCORE += 50
        elif user_win[computer] == user:
            result = WIN
            SCORE += 100
        else:
            result = LOSE

        self.leaderBoard[self.player_name] = SCORE
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

    def rating(self):
        if self.player_name in self.leaderBoard.keys():
            return f"your rating: {self.leaderBoard[self.player_name]}"
        else:
            return f"your rating: 0"


if __name__ == '__main__':
    Game().play()
