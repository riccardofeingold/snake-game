from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 28, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

        super().__init__()
        self.setposition((0, 250))
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increaseScore(self):
        self.score += 1
        self.update_scoreboard()
